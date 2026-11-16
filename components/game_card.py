from pathlib import Path
from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QFrame, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)

ROOT = Path(__file__).resolve().parent.parent
COVERS_DIR = ROOT / "resources" / "images"

class GameCard(QFrame):
    edit_requested = Signal(int)
    delete_requested = Signal(int)

    def __init__(self, game):
        super().__init__()
        self.game_id = game["id"]
        self.setObjectName("gameCard")
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setMinimumWidth(220)
        self.setMaximumWidth(320)

        layout = QVBoxLayout(self)
        layout.setSpacing(9)

        cover = QLabel()
        cover.setObjectName("coverPlaceholder")
        cover.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cover.setMinimumHeight(200)
        cover.setScaledContents(False)

        caratula = game["caratula"]
        if caratula:
            nombre = Path(caratula).name
            ruta = COVERS_DIR / nombre
            if ruta.exists():
                pixmap = QPixmap(str(ruta))
                if not pixmap.isNull():
                    cover.setPixmap(
                        pixmap.scaled(
                            250, 300,
                            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
                            Qt.TransformationMode.SmoothTransformation
                        )
                    )
                else:
                    cover.setText("🎮")
            else:
                cover.setText("🎮")
        else:
            cover.setText("🎮")

        layout.addWidget(cover)

        title = QLabel(game["titulo"])
        title.setObjectName("cardTitle")
        title.setWordWrap(True)
        layout.addWidget(title)

        info = QLabel(
            f'{game["genero"] or "Sin género"} • '
            f'{game["plataforma"] or "Sin plataforma"}'
        )
        info.setObjectName("muted")
        info.setWordWrap(True)
        layout.addWidget(info)

        year = str(game["anio"]) if game["anio"] else "Año no indicado"
        rating = f'{float(game["puntuacion"] or 0):g}/5 ★'
        meta = QLabel(f"{year} · {rating}")
        meta.setObjectName("rating")
        layout.addWidget(meta)

        buttons = QHBoxLayout()
        edit_btn = QPushButton("Editar")
        edit_btn.setObjectName("secondaryButton")
        delete_btn = QPushButton("Eliminar")
        delete_btn.setObjectName("dangerButton")

        edit_btn.clicked.connect(lambda: self.edit_requested.emit(self.game_id))
        delete_btn.clicked.connect(lambda: self.delete_requested.emit(self.game_id))

        buttons.addWidget(edit_btn)
        buttons.addWidget(delete_btn)
        layout.addLayout(buttons)