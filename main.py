import tkinter as tk
from tkinter import ttk

def open_speed_converter():
    CONVERSIONS = {
        'km/h': {
            'km/h': 1,
            'm/s': 0.277778,
            'mph': 0.621371,
            'ft/s': 0.911344
        },
        'm/s': {
            'km/h': 3.6,
            'm/s': 1,
            'mph': 2.23694,
            'ft/s': 3.28084
        },
        'mph': {
            'km/h': 1.60934,
            'm/s': 0.44704,
            'mph': 1,
            'ft/s': 1.46667
        },
        'ft/s': {
            'km/h': 1.09728,
            'm/s': 0.3048,
            'mph': 0.681818,
            'ft/s': 1
        }
    }

    def calculate(*args):
        try:
            value = float(input_value.get())
            input_unit = input_unit_value.get()
            output_unit = output_unit_value.get()
            output_value.set(value * CONVERSIONS[input_unit][output_unit])
        except ValueError:
            print("error occurred in calculator: "+ str(ValueError))
            pass

    window = tk.Toplevel(root)
    window.title("Speed Converter")

    mainframe = ttk.Frame(window, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    input_value = tk.StringVar()
    output_value = tk.StringVar()
    input_unit_value = tk.StringVar()
    output_unit_value = tk.StringVar()

    input_entry = ttk.Entry(mainframe, width=7, textvariable=input_value)
    input_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

    output_label = ttk.Label(mainframe, textvariable=output_value)
    output_label.grid(column=2, row=2, sticky=(tk.W, tk.E))

    ttk.Label(mainframe, text="is equivalent to").grid(column=3, row=1, sticky=tk.E)
    ttk.Label(mainframe, text="in").grid(column=3, row=2, sticky=tk.E)

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=tk.W)

    ttk.OptionMenu(mainframe, input_unit_value, 'km/h', 'm/s', 'mph', 'ft/s').grid(column=1, row=1, sticky=tk.W)
    ttk.OptionMenu(mainframe, output_unit_value, 'km/h', 'm/s', 'mph', 'ft/s').grid(column=1, row=2, sticky=tk.W)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    input_entry.focus()
    window.bind('<Return>', calculate)

def open_weight_converter():
    CONVERSIONS = {
        'g': {
            'g': 1,
            'kg': 0.001,
            'pound': 0.0022046226,
            'ounce': 0.0352739619,
            'mesghal': 0.21701389,
            'charak': 0.0013333333,
        },
        'kg': {
            'g': 1000,
            'kg': 1,
            'pound': 2.20462262,
            'ounce': 35.2739619,
            'mesghal': 217.01389,
            'charak': 1.3333333,
        },
        'pound': {
            'g': 453.5923704,
            'kg': 0.4535923704,
            'pound': 1,
            'ounce': 15.9999999909,
            'mesghal': 98.43584477,
            'charak': 0.6047898257,
        },
        'ounce': {
            'g': 28.3495231648,
            'kg': 0.0283495232,
            'pound': 0.0625,
            'ounce': 1,
            'mesghal': 6.1522403,
            'charak': 0.03779936,
        },
        'mesghal': {
            'g': 4.6079999764,
            'kg': 0.004608,
            'pound': 0.010158901,
            'ounce': 0.1625424156,
            'mesghal': 1,
            'charak': 0.006144,
        },
        'charak': {
            'g': 750,
            'kg': 0.75,
            'pound': 1.6534669691,
            'ounce': 26.4554714911,
            'mesghal': 162.7604179069,
            'charak': 1,
        },
    }
    def calculate(*args):
        try:
            value = float(input_value.get())
            input_unit = input_unit_value.get()
            output_unit = output_unit_value.get()
            output_value.set(value * CONVERSIONS[input_unit][output_unit])
        except ValueError:
            print("error accure in calculateor"+ str(ValueError))
            pass

    window = tk.Toplevel(root)
    window.title("weight Converter")

    mainframe = ttk.Frame(window, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    input_value = tk.StringVar()
    output_value = tk.StringVar()
    input_unit_value = tk.StringVar()
    output_unit_value = tk.StringVar()

    input_entry = ttk.Entry(mainframe, width=7, textvariable=input_value)
    input_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

    output_label = ttk.Label(mainframe, textvariable=output_value)
    output_label.grid(column=2, row=2, sticky=(tk.W, tk.E))

    ttk.Label(mainframe, text="is equivalent to").grid(column=3, row=1, sticky=tk.E)
    ttk.Label(mainframe, text="in").grid(column=3, row=2, sticky=tk.E)

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=tk.W)

    ttk.OptionMenu(mainframe, input_unit_value, 'g', 'kg', 'pound', 'ounce', 'mesghal', 'charak').grid(column=1, row=1, sticky=tk.W)
    ttk.OptionMenu(mainframe, output_unit_value, 'g', 'kg', 'pound', 'ounce', 'mesghal', 'charak').grid(column=1, row=2, sticky=tk.W)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    input_entry.focus()
    window.bind('<Return>', calculate)
    
def open_length_converter():
    # Conversion Factors
    CONVERSIONS = {
        'cm': {
            'cm': 1,
            'm': 0.01,
            'km': 0.00001,
            'inch': 0.393701,
            'feet': 0.0328084,
            'mile': 0.0000062137,
            'yard': 0.01093613298,
            'ligh_year': 1.057000834e-18,
        },
        'm': {
            'cm': 100,
            'm': 1,
            'km': 0.001,
            'inch': 39.3701,
            'feet': 3.28084,
            'mile': 0.000621371,
            'yard': 1.093613298,
            'ligh_year': 1.057000834e-16,
            
        },
        'km': {
            'cm': 100000,
            'm': 1000,
            'km': 1,
            'inch': 39370.1,
            'feet': 3280.84,
            'mile': 0.621371,
            'yard': 1093.613298,
            'ligh_year': 1.057000834e-13,
            
        },
        'inch': {
            'cm': 2.54,
            'm': 0.0254,
            'km': 0.0000254,
            'inch': 1,
            'feet': 0.0833333334,
            'mile': 0.0000157828,
            'yard': 0.0277777778,
            'ligh_year': 2.6847821183707394e-18,
        },
        'feet': {
            'cm': 30.48,
            'm': 0.3048,
            'km': 0.0003048,
            'inch': 12,
            'feet': 1,
            'mile': 0.0001893939,
            'yard': 0.3333333334,
            'ligh_year': 3.2217385420448865e-17,
        },
        'mile': {
            'cm': 160934.3979894787,
            'm': 1609.3439798948,
            'km': 1.6093439799,
            'inch': 63359.9992082028,
            'feet': 5279.9999340169,
            'mile': 1,
            'yard': 1759.999977952,
            'ligh_year': 1.7010779289416698e-13,
        },
        'yard': {
            'cm': 91.44,
            'm': 0.9144,
            'km': 0.0009144,
            'inch': 36,
            'feet': 3,
            'mile': 0.0005681818,
            'yard': 1,
            'ligh_year': 9.665215626429257e-17,
        },
        'ligh_year': {
            'cm': 0,
            'm': 0,
            'km': 9460730472801.121,
            'inch': 0,
            'feet': 0,
            'mile': 5878625446761,
            'yard': 0,
            'ligh_year': 1,
        },
    }

    def calculate(*args):
        try:
            value = float(input_value.get())
            input_unit = input_unit_value.get()
            output_unit = output_unit_value.get()
            output_value.set(value * CONVERSIONS[input_unit][output_unit])
        except ValueError:
            print("error accure in calculateor"+ str(ValueError))
            pass

    window = tk.Toplevel(root)
    window.title("Length Converter")

    mainframe = ttk.Frame(window, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    input_value = tk.StringVar()
    output_value = tk.StringVar()
    input_unit_value = tk.StringVar()
    output_unit_value = tk.StringVar()

    input_entry = ttk.Entry(mainframe, width=7, textvariable=input_value)
    input_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))

    output_label = ttk.Label(mainframe, textvariable=output_value)
    output_label.grid(column=2, row=2, sticky=(tk.W, tk.E))

    ttk.Label(mainframe, text="is equivalent to").grid(column=3, row=1, sticky=tk.E)
    ttk.Label(mainframe, text="in").grid(column=3, row=2, sticky=tk.E)

    ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=tk.W)

    ttk.OptionMenu(mainframe, input_unit_value, 'cm', 'm', 'km', 'inch', 'feet', 'mile', 'yard', 'ligh_year').grid(column=1, row=1, sticky=tk.W)
    ttk.OptionMenu(mainframe, output_unit_value, 'cm', 'm', 'km', 'inch', 'feet', 'mile', 'yard', 'ligh_year').grid(column=1, row=2, sticky=tk.W)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    input_entry.focus()
    window.bind('<Return>', calculate)


root = tk.Tk()
root.title("Unit Converter")
root.geometry('300x100')

ttk.Button(root, text="Length Converter", command=open_length_converter).pack()
ttk.Button(root, text="Weight Converter", command=open_weight_converter).pack()
ttk.Button(root, text="Speed Converter", command=open_speed_converter).pack()


root.mainloop()
