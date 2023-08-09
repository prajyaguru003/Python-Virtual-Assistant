import PySimpleGUI as sg
import wolframalpha
import wikipedia

client = wolframalpha.Client("Add your AppID from Wolfram Alpha") # Add your AppId from Wolfram Alpha

# Starting Window where you choose between the two API's
sg.theme('GreenMono')
# Creates the Starting layout
ask = [     [sg.Text('Which Website will you use?')],
            [sg.Button('Wolfram Alpha'), sg.Button('Wikipedia')] ]
window = sg.Window('Trebuchet VA', ask)
event, values = window.read()

if event in ('Wolfram Alpha'): # if Wolfram Alpha is chosen

    sg.theme('DarkAmber')
    # Basic layout of the Wolfram Alpha window
    layout = [  [sg.Text('Wolfram Alpha locked on')],
                [sg.Text('Type a Command'), sg.InputText()],
                [sg.Button('Enter'), sg.Button('Cancel')] ]

    window = sg.Window('Trebuchet VA', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        try:
            wolf_res = client.query(values[0]) # Searches Wolfram Alpha for the value inputed
            sg.Popup('Results for "'+values[0]+'":', next(wolf_res.results).text) # Displays the SubPods from the responce
        except:
            sg.Popup('Results for "'+values[0]+'" is inconclusive; Please try again') # If the Input doesn't exsist

    window.close()
elif event in ('Wikipedia'): # if Wikipedia is chosen

    sg.theme('LightBlue')
    # Basic layout of the Wikipedia window
    layout = [  [sg.Text('Wikipedia locked on')],
                [sg.Text('Type a Command'), sg.InputText()],
                [sg.Text('How many sentences do you want?'), sg.InputText()],
                [sg.Text('(more sentences = more info)')],
                [sg.Button('Enter'), sg.Button('Cancel')] ]

    window = sg.Window('Trebuchet VA', layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        try:
            if values[1] == 0:
                values[1] = 1
            wika_res = wikipedia.summary(values[0], sentences = values[1]) # Gets the Wikipedia summary for the value inputed
            sg.Popup('Results for "'+values[0]+'":', wika_res, 'Link to page: '+wikipedia.page(values[0]).url) # Displays the Summary ristricted by the sentence count with the Link to the page
        except:
            try: # The API of Wikipedia has a few bugs so this is just to check if an answer to the input exists

                wolf_res = client.query(values[0]) # Searches Wolfram Alpha for the value inputed
                sg.Popup('Results for "'+values[0]+'":', next(wolf_res.results).text, 'Taken from Wolfram Alpha') # Displays the SubPods from the Query
            except:
                sg.Popup('Results for "'+values[0]+'" is inconclusive; Please try again') # If the input doesn't exist


    window.close()
else: # if you exit the tab, closes the Starting program
    window.close()