# geniushaey_tk.py
# 연차계산기 (구조만 대충) - exe 배포용

import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import date
import core


def run_calculation():
    try:
        path = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx")])
        if not path:
            return

        emp = core.Employee(
            name="직원",
            first_hire_date=date.fromisoformat(entry_hire.get()),
            period_type=period_var.get(),
            schedule_key=entry_denom.get()
        )

        worklog = core.read_worklog(path)
        result = core.calculate_annual_leave(emp, worklog, int(entry_year.get()))

        txt.delete("1.0", tk.END)
        for k, v in result.items():
            txt.insert(tk.END, f"{k}: {v}\n")

    except Exception as e:
        messagebox.showerror("오류", str(e))


root = tk.Tk()
root.title("연차계산기 (구조만 대충) - 고해영 천재")

tk.Label(root, text="부여연도").grid(row=0, column=0)
entry_year = tk.Entry(root)
entry_year.insert(0, "2026")
entry_year.grid(row=0, column=1)

tk.Label(root, text="최초임용일 (YYYY-MM-DD)").grid(row=1, column=0)
entry_hire = tk.Entry(root)
entry_hire.grid(row=1, column=1)

tk.Label(root, text="분모키 (예: FULLTIME_260)").grid(row=2, column=0)
entry_denom = tk.Entry(root)
entry_denom.insert(0, "FULLTIME_260")
entry_denom.grid(row=2, column=1)

period_var = tk.StringVar(value="SCHOOL_YEAR")
tk.Radiobutton(root, text="학교형", variable=period_var, value="SCHOOL_YEAR").grid(row=3, column=0)
tk.Radiobutton(root, text="기관형", variable=period_var, value="CALENDAR_YEAR").grid(row=3, column=1)

tk.Button(root, text="근무상황목록 선택 & 계산", command=run_calculation).grid(row=4, column=0, columnspan=2)

txt = tk.Text(root, height=10, width=50)
txt.grid(row=5, column=0, columnspan=2)

root.mainloop()
