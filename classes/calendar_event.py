from PyQt6.QtWidgets import QApplication, QGraphicsView, QGraphicsScene, QGraphicsRectItem
from PyQt6.QtGui import QBrush, QColor
from PyQt6.QtCore import Qt, QPointF
import sys

class DraggableEvent(QGraphicsRectItem):
    def __init__(self, x, y, w, h, title):
        super().__init__(0, 0, w, h)
        self.setPos(x, y)
        self.title = title
        self.setBrush(QBrush(QColor("lightblue")))

        self.setFlag(QGraphicsRectItem.GraphicsItemFlag.ItemIsSelectable)
        self.setAcceptHoverEvents(True)

        self.drag_offset = QPointF()

    def mousePressEvent(self, event):
        # Store where inside the item the mouse was clicked
        self.drag_offset = event.scenePos() - self.pos()
        event.accept()

    def mouseMoveEvent(self, event):
        # Move item while keeping the same click offset
        self.setPos(event.scenePos() - self.drag_offset)
        event.accept()

    def mouseReleaseEvent(self, event):
        local_pos = self.pos()
        day_width = 100 # get this directly from the calendar eventually
        time_height = 40 # get this directly from the calendar eventually
        delta_x = local_pos.x() % day_width
        print(f"delta_x: {delta_x}")
        delta_y = local_pos.y() % time_height
        if delta_x >= day_width / 2:
            delta_x =-1*(day_width - delta_x)
        if delta_y >= time_height / 2:
            delta_y =-1*(time_height - delta_y)

        self.setPos(local_pos.x()-delta_x,local_pos.y()-delta_y)

class CalendarView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)

        self.draw_week_grid()

        # Add a sample event
        element = DraggableEvent(50, 50, 100, 40, "Meeting")
        self.scene.addItem(element)

    def draw_week_grid(self):
        day_width = 100
        time_height = 40
        rows = 10   # example time slots
        cols = 7

        for c in range(cols):
            for r in range(rows):
                self.scene.addRect(
                    c * day_width, r * time_height,
                    day_width, time_height
                )