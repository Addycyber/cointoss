import sys
import random
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QSpinBox, QPushButton,
    QVBoxLayout, QTextEdit, QHBoxLayout
)
from PyQt5.QtGui import QFont

class CoinTossApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Virtual Coin Toss Simulator")
        self.init_ui()

    def init_ui(self):
        # Instruction label
        self.instruction_label = QLabel("Enter number of coin tosses:")
        self.instruction_label.setFont(QFont("Arial", 12))

        # Spin box for number of tosses
        self.spinBox = QSpinBox()
        self.spinBox.setRange(0, 10000)
        self.spinBox.setValue(10)
        self.spinBox.setFont(QFont("Arial", 12))

        # Toss button
        self.toss_button = QPushButton("Toss")
        self.toss_button.setFont(QFont("Arial", 12))
        self.toss_button.clicked.connect(self.simulate_tosses)

        # Results display (read-only)
        self.results_text = QTextEdit()
        self.results_text.setReadOnly(True)
        self.results_text.setFont(QFont("Consolas", 12))

        # Summary label for counts and percentages
        self.summary_label = QLabel("Summary:")
        self.summary_label.setFont(QFont("Arial", 12))

        # Clear button to reset the results
        self.clear_button = QPushButton("Clear")
        self.clear_button.setFont(QFont("Arial", 12))
        self.clear_button.clicked.connect(self.clear_results)

        # Layouts
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.instruction_label)
        input_layout.addWidget(self.spinBox)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.toss_button)
        button_layout.addWidget(self.clear_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.results_text)
        main_layout.addWidget(self.summary_label)

        self.setLayout(main_layout)

    def simulate_tosses(self):
        num_tosses = self.spinBox.value()
        if num_tosses <= 0:
            self.results_text.setText("No tosses performed.")
            self.summary_label.setText("Summary:")
            return

        results = []
        heads_count = 0
        tails_count = 0

        # Simulate coin tosses
        for _ in range(num_tosses):
            outcome = random.choice(["Heads", "Tails"])
            results.append(outcome)
            if outcome == "Heads":
                heads_count += 1
            else:
                tails_count += 1

        # Display the individual toss results
        self.results_text.setText(" ".join(results))

        # Calculate percentages
        heads_percentage = (heads_count / num_tosses) * 100
        tails_percentage = (tails_count / num_tosses) * 100

        # Update summary label with counts and percentages
        summary_text = (
            f"Total Tosses: {num_tosses}\n"
            f"Heads: {heads_count} ({heads_percentage:.2f}%)\n"
            f"Tails: {tails_count} ({tails_percentage:.2f}%)"
        )
        self.summary_label.setText(summary_text)

    def clear_results(self):
        self.results_text.clear()
        self.summary_label.setText("Summary:")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoinTossApp()
    window.resize(500, 400)
    window.show()
    sys.exit(app.exec_())
