import sys
import shutil
from pathlib import Path

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QFile, QObject, Qt
from PySide6.QtUiTools import QUiLoader

from PySide6.QtWidgets import (
    QApplication, QDialog, QMessageBox, QFileDialog,
    QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, 
    QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox, QPushButton
)

import database
from components.game_card import GameCard

ROOT = Path(__file__).resolve().parent
COVERS_DIR = ROOT / "resources" / "images"

STYLES = """
QMainWindow, QDialog {
    background: #101522;
}

QWidget {
    color: #e8edf7;
    font-family: DejaVu Sans;
    font-size: 10pt;
}

QLabel#logoLabel {
    font-size: 25pt;
    font-weight: 800;
    color: #8b9cff;
}

QLabel#subtitleLabel, QLabel#muted {
    color: #9aa6bd;
}

QLabel#countLabel {
    color: #aeb9d0;
    font-weight: 600;
}

QLabel#formTitle {
    font-size: 18pt;
    font-weight: 700;
    color: #8b9cff;
}

QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox {
    background: #1b2435;
    border: 1px solid #34415a;
    border-radius: 8px;
    padding: 9px;
}

QPushButton {
    border: 0;
    border-radius: 8px;
    padding: 9px 13px;
    font-weight: 600;
}

QPushButton#addButton {
    background: #6879e8;
    color: white;
}

QPushButton#secondaryButton {
    background: #29364e;
    color: white;
}

QPushButton#dangerButton {
    background: #512d3b;
    color: #ffb7c5;
}

QFrame#gameCard {
    background: #1a2333;
    border: 1px solid #2d3a52;
    border-radius: 13px;
}

QLabel#coverPlaceholder {
    background: #252f46;
    border-radius: 9px;
    font-size: 32pt;
}

QLabel#cardTitle {
    font-size: 12pt;
    font-weight: 700;
}

QLabel#rating {
    color: #f4c96b;
    font-weight: 700;
}

QScrollArea {
    border: none;
    background: transparent;
}
"""


def load_ui(filename, parent=None):
    loader = QUiLoader()
    ui_file = QFile(str(ROOT / "ui" / filename))

    if not ui_file.open(QFile.OpenModeFlag.ReadOnly):
        raise RuntimeError(f"No se pudo abrir la interfaz: {filename}")

    widget = loader.load(ui_file, parent)
    ui_file.close()

    if widget is None:
        raise RuntimeError(loader.errorString())

    for child in widget.findChildren(QObject):
        name = child.objectName()
        if name:
            setattr(widget, name, child)

    return widget


class GameDialog(QDialog):
    GENRES = ["Acción", "Aventura", "RPG", "Deportes", "Estrategia", "Simulación", "Sandbox", "Terror", "Metroidvania", "Carreras", "Plataformas"]
    PLATFORMS = ["PC", "PlayStation 5", "PlayStation 4", "Xbox Series X/S", "Xbox One", "Nintendo Switch", "Nintendo 3DS", "Móvil"]

    def __init__(self, parent=None, game=None):
        super().__init__(parent)
        self.game = game
        
        # Configuración básica del diálogo
        self.setWindowTitle("Editar videojuego" if game else "Añadir videojuego")
        self.setMinimumWidth(450)
        
        # --- CREAMOS TODA LA INTERFAZ POR CÓDIGO ---
        layout = QVBoxLayout(self)
        
        # Título de la ventana
        self.lbl_title = QLabel("Editar videojuego" if game else "Añadir videojuego")
        self.lbl_title.setObjectName("formTitle")
        layout.addWidget(self.lbl_title)

        # Formulario
        form_layout = QFormLayout()
        
        self.titleInput = QLineEdit()
        self.titleInput.setPlaceholderText("Ej: The Legend of Zelda")
        
        self.genreInput = QComboBox()
        self.genreInput.addItems(self.GENRES)
        
        self.platformInput = QComboBox()
        self.platformInput.addItems(self.PLATFORMS)
        
        self.yearInput = QSpinBox()
        self.yearInput.setRange(1958, 2100)
        self.yearInput.setValue(2024)
        
        self.ratingInput = QDoubleSpinBox()
        self.ratingInput.setRange(0.0, 5.0)
        self.ratingInput.setSingleStep(0.5)
        
        self.coverInput = QLineEdit()
        self.coverInput.setPlaceholderText("Sin archivo seleccionado")
        self.coverInput.setReadOnly(True)
        
        self.browseCoverButton = QPushButton("Examinar…")
        self.browseCoverButton.clicked.connect(self.select_cover)
        
        cover_layout = QHBoxLayout()
        cover_layout.addWidget(self.coverInput)
        cover_layout.addWidget(self.browseCoverButton)
        
        form_layout.addRow("Título *", self.titleInput)
        form_layout.addRow("Género", self.genreInput)
        form_layout.addRow("Plataforma", self.platformInput)
        form_layout.addRow("Año", self.yearInput)
        form_layout.addRow("Puntuación", self.ratingInput)
        form_layout.addRow("Carátula", cover_layout)
        
        layout.addLayout(form_layout)
        
        # Vista previa de la foto
        self.coverPreview = QLabel("Sin carátula")
        self.coverPreview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coverPreview.setFixedSize(120, 160)
        layout.addWidget(self.coverPreview, alignment=Qt.AlignmentFlag.AlignCenter)

        # Botones finales
        botones_layout = QHBoxLayout()
        self.saveButton = QPushButton("Guardar")
        self.saveButton.setObjectName("addButton") # Para que herede el color azul
        self.saveButton.clicked.connect(self.save)
        
        self.cancelButton = QPushButton("Cancelar")
        self.cancelButton.setObjectName("secondaryButton") # Color gris
        self.cancelButton.clicked.connect(self.reject)
        
        botones_layout.addStretch()
        botones_layout.addWidget(self.cancelButton)
        botones_layout.addWidget(self.saveButton)
        
        layout.addLayout(botones_layout)

        # --- SI ES EDICIÓN, RELLENAMOS LOS DATOS ---
        if game:
            self.titleInput.setText(game["titulo"])
            self.genreInput.setCurrentText(game["genero"] or "")
            self.platformInput.setCurrentText(game["plataforma"] or "")
            self.yearInput.setValue(game["anio"] or 2024)
            self.ratingInput.setValue(float(game["puntuacion"] or 0))
            if game["caratula"]:
                self.coverInput.setText(game["caratula"])
                self.update_cover_preview(game["caratula"])

    def save(self):
        title = self.titleInput.text().strip()
        if not title:
            QMessageBox.warning(self, "Dato obligatorio", "Escribe el título del videojuego.")
            return
        self.accept()

    def values(self):
        title = self.titleInput.text().strip()
        year = self.yearInput.value()
        caratula = self.coverInput.text().strip() or None

        return (
            title,
            self.genreInput.currentText().strip(),
            self.platformInput.currentText().strip(),
            year,
            self.ratingInput.value(),
            caratula
        )

    def select_cover(self):
        COVERS_DIR.mkdir(parents=True, exist_ok=True)
        ruta_origen, _ = QFileDialog.getOpenFileName(
            self, "Seleccionar carátula", str(ROOT), "Imágenes (*.png *.jpg *.jpeg *.webp)"
        )
        if not ruta_origen:
            return

        origen = Path(ruta_origen)
        destino = COVERS_DIR / origen.name
        try:
            shutil.copy2(origen, destino)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo copiar la imagen:\n{e}")
            return

        self.coverInput.setText(destino.name)
        self.update_cover_preview(destino.name)

    def update_cover_preview(self, filename):
        ruta = COVERS_DIR / filename
        pixmap = QPixmap(str(ruta))
        if pixmap.isNull():
            self.coverPreview.setText("Sin carátula")
            self.coverPreview.setPixmap(QPixmap())
        else:
            self.coverPreview.setPixmap(
                pixmap.scaled(120, 160, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            )


class MainController:

    def __init__(self):
        self.window = load_ui("main_window.ui")
        self.window.setStyleSheet(STYLES)

        icon_path = ROOT / "resources" / "icons" / "icono.png"
        if icon_path.exists():
            self.window.setWindowIcon(QIcon(str(icon_path)))

        self.window.addButton.clicked.connect(self.add_game)
        self.window.searchInput.textChanged.connect(self.refresh)
        self.window.genreFilter.currentTextChanged.connect(self.refresh)
        self.window.platformFilter.currentTextChanged.connect(self.refresh)

        self.refresh_filters()
        self.refresh()

    def clear_cards(self):
        layout = self.window.cardsLayout
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

    def refresh_filters(self):
        genre = self.window.genreFilter.currentText()
        platform = self.window.platformFilter.currentText()

        self.window.genreFilter.blockSignals(True)
        self.window.platformFilter.blockSignals(True)

        self.window.genreFilter.clear()
        self.window.platformFilter.clear()

        self.window.genreFilter.addItems(["Todos"] + database.get_filter_values("genero"))
        self.window.platformFilter.addItems(["Todas"] + database.get_filter_values("plataforma"))

        self.window.genreFilter.setCurrentText(genre if genre else "Todos")
        self.window.platformFilter.setCurrentText(platform if platform else "Todas")

        self.window.genreFilter.blockSignals(False)
        self.window.platformFilter.blockSignals(False)

    def refresh(self):
        self.clear_cards()

        games = database.get_games(
            self.window.searchInput.text(),
            self.window.genreFilter.currentText(),
            self.window.platformFilter.currentText()
        )

        for index, game in enumerate(games):
            card = GameCard(game)
            card.edit_requested.connect(self.edit_game)
            card.delete_requested.connect(self.remove_game)
            self.window.cardsLayout.addWidget(card, index // 3, index % 3)

        self.window.countLabel.setText(f"{len(games)} videojuego(s) encontrado(s)")

    def add_game(self):
        dialog = GameDialog(self.window)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            try:
                database.add_game(*dialog.values())
            except Exception as e:
                QMessageBox.critical(self.window, "Error", f"No se pudo guardar:\n{e}")
                return

            self.refresh_filters()
            self.refresh()
            QMessageBox.information(self.window, "Correcto", "Videojuego añadido correctamente.")

    def edit_game(self, game_id):
        game = database.get_game(game_id)
        if not game:
            return

        dialog = GameDialog(self.window, game)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            try:
                database.update_game(game_id, *dialog.values())
            except Exception as e:
                QMessageBox.critical(self.window, "Error", f"No se pudo actualizar:\n{e}")
                return

            self.refresh_filters()
            self.refresh()
            QMessageBox.information(self.window, "Correcto", "Videojuego actualizado correctamente.")

    def remove_game(self, game_id):
        game = database.get_game(game_id)
        if not game:
            return

        answer = QMessageBox.question(
            self.window, "Confirmar eliminación",
            f'¿Seguro que quieres eliminar «{game["titulo"]}»?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )

        if answer == QMessageBox.StandardButton.Yes:
            database.delete_game(game_id)
            self.refresh_filters()
            self.refresh()
            QMessageBox.information(self.window, "Eliminado", "Videojuego eliminado correctamente.")


def sincronizar_fotos():
    """
    Enlaza los archivos de la carpeta 'images' con los juegos.
    Incluye reglas exactas para que ningún juego se quede sin foto.
    """
    import sqlite3
    conn = sqlite3.connect(database.DB_PATH)
    cur = conn.cursor()

    # Diccionario con la palabra clave en el título y el nombre exacto de la foto
    equivalencias_exactas = {
        "animal crossing": "AnimalCrossing.jpeg",
        "elden ring": "EldenRing.jpeg",
        "hollow knight": "HollowKnight.jpeg",
        "minecraft": "Minecraft.jpeg",
        "red dead": "RedDeadRedemption2.jpeg",
        "legend": "TheLegend.jpeg",
        "zelda": "TheLegend.jpeg",
        "witcher": "TheWitcher3.jpeg"
    }

    cur.execute("SELECT id, titulo FROM videojuegos")
    juegos = cur.fetchall()

    if COVERS_DIR.exists():
        archivos = [f.name for f in COVERS_DIR.glob("*") if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp")]
        
        for juego_id, titulo in juegos:
            titulo_limpio = titulo.lower().replace(" ", "").replace(":", "")
            foto_asignada = None

            # 1. Buscar usando nuestra lista de equivalencias manuales
            for key, nombre_foto in equivalencias_exactas.items():
                if key in titulo.lower():
                    foto_asignada = nombre_foto
                    break
            
            # 2. Si por alguna razón no estaba en la lista, buscar automáticamente
            if not foto_asignada:
                for archivo in archivos:
                    archivo_limpio = archivo.lower().replace(" ", "").replace(":", "")
                    if titulo_limpio in archivo_limpio or archivo_limpio.startswith(titulo_limpio):
                        foto_asignada = archivo
                        break
            
            # 3. Guardar el nombre del archivo en la Base de Datos
            if foto_asignada:
                cur.execute("UPDATE videojuegos SET caratula=? WHERE id=?", (foto_asignada, juego_id))

    conn.commit()
    conn.close()


def main():
    database.initialize_database()
    
    # Enlaza las fotos automáticamente al arrancar
    sincronizar_fotos()

    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    icon_path = ROOT / "resources" / "icons" / "icono.png"
    if icon_path.exists():
        app.setWindowIcon(QIcon(str(icon_path)))

    controller = MainController()
    controller.window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()