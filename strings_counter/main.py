from pyscript import document


def count(event):
    input_text = document.querySelector("#strinput")
    txt = input_text.value
    output_div = document.querySelector("#strlen_output")
    output_div.innerText = len(txt)


def clear(event):
    input_text = document.querySelector("#strinput")
    input_text.value = ""
    output_div = document.querySelector("#strlen_output")
    output_div.innerText = "0"
