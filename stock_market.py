import yfinance as yf
import tkinter as tk
from tkinter import ttk

def get_stock_price():
    ticker = ticker_entry.get().upper()
    if not ticker:
        label.config(text="Please enter a ticker symbol.")
        return

    try:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period="1d")['Close'][0]
        label.config(text=f"The current price of {ticker} is ${current_price:.2f}")
    except Exception as e:
        label.config(text=f"Error fetching data: {e}")

root = tk.Tk()
root.title("Real-time Stock Price Checker")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

ticker_label = ttk.Label(mainframe, text="Enter a ticker symbol:")
ticker_label.grid(column=0, row=0, sticky=(tk.W, tk.E))

ticker_entry = ttk.Entry(mainframe, width=20)
ticker_entry.grid(column=0, row=1, sticky=(tk.W, tk.E))

get_price_button = ttk.Button(mainframe, text="Get Price", command=get_stock_price)
get_price_button.grid(column=0, row=2, sticky=tk.W)

label = ttk.Label(mainframe, text="")
label.grid(column=0, row=3, sticky=(tk.W, tk.E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
