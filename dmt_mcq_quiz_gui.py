
import tkinter as tk
from tkinter import messagebox
import random
import os
import csv

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.master.title("DMT MCQ Quiz")
        self.questions = random.sample(questions, len(questions))
        self.current = 0
        self.score = 0
        self.results = []

        self.question_var = tk.StringVar()
        self.metadata_var = tk.StringVar()
        self.answer_var = tk.StringVar()

        self.meta_label = tk.Label(master, textvariable=self.metadata_var, font=("Arial", 10, "italic"))
        self.meta_label.pack(pady=5)

        self.question_label = tk.Label(master, textvariable=self.question_var, wraplength=500, font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.radio_buttons = []
        self.choice_vars = ["A", "B", "C", "D"]
        for choice in self.choice_vars:
            b = tk.Radiobutton(master, text="", variable=self.answer_var, value=choice, font=("Arial", 12))
            b.pack(anchor='w')
            self.radio_buttons.append(b)

        self.submit_btn = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_btn.pack(pady=10)

        self.load_question()

    def load_question(self):
        q = self.questions[self.current]
        self.metadata_var.set(q["metadata"])
        self.question_var.set(f"Q{self.current + 1}: {q['question']}")
        for i, key in enumerate(self.choice_vars):
            self.radio_buttons[i].config(text=f"{key}. {q['choices'][key]}")
        self.answer_var.set("")

    def check_answer(self):
        if not self.answer_var.get():
            messagebox.showwarning("Warning", "Please select an answer.")
            return

        q = self.questions[self.current]
        user_answer = self.answer_var.get()
        correct = user_answer == q["answer"]

        if correct:
            self.score += 1
            messagebox.showinfo("Correct!", "✅ That's correct!")
        else:
            messagebox.showerror("Incorrect", f"❌ The correct answer was {q['answer']}.")

        self.results.append({
            "Question": q["question"],
            "Source": q["metadata"],
            "Correct Answer": q["answer"],
            "Your Answer": user_answer,
            "Result": "Correct" if correct else "Incorrect"
        })

        self.current += 1
        if self.current < len(self.questions):
            self.load_question()
        else:
            self.end_quiz()

    def end_quiz(self):
        messagebox.showinfo("Quiz Complete", f"You scored {self.score}/{len(self.questions)}")
        with open("quiz_results_gui.csv", "w", newline='', encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["Question", "Source", "Correct Answer", "Your Answer", "Result"])
            writer.writeheader()
            writer.writerows(self.results)
        self.master.quit()

def load_questions(filename):
    with open(filename, "r", encoding="utf-8") as f:
        blocks = f.read().strip().split("\n\n")
    questions = []
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 6:
            continue
        metadata = lines[0].strip()
        question = lines[1].strip()[3:]
        choices = {
            'A': lines[2].strip()[3:],
            'B': lines[3].strip()[3:],
            'C': lines[4].strip()[3:],
            'D': lines[5].strip()[3:]
        }
        answer_line = [l for l in lines if l.strip().startswith("Answer:")]
        answer = answer_line[0].split(":")[1].strip().upper() if answer_line else "X"
        questions.append({
            "metadata": metadata,
            "question": question,
            "choices": choices,
            "answer": answer
        })
    return questions

if __name__ == "__main__":
    question_file = "DMT_MCQ_QuestionBank.txt"
    if not os.path.exists(question_file):
        print("❌ Question bank not found.")
    else:
        questions = load_questions(question_file)
        root = tk.Tk()
        app = QuizApp(root, questions)
        root.mainloop()
