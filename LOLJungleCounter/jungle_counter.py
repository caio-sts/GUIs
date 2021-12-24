import PySimpleGUI as sg
import datetime
import time
import threading

# Auxiliary functions
def regresstimer(window,key,tempo=5):
        while (tempo > 0):
            window[key].update(str(datetime.timedelta(seconds=tempo)))
            tempo -= 1
            time.sleep(1)
        window[key].update('Tempo')

def reg(key, tempo=300):
    threading.Thread(target=regresstimer, args=(window,key, tempo), daemon=True).start()

# GUI Style
sg.theme('DarkAmber')   

layout = [[sg.Text('Blue Side')],
    [sg.InputText('Grompe', key='I1', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='1', enable_events=True, pad=(5,5)), sg.Button('Start 1', enable_events=True, pad=(5,5))],
    [sg.InputText('Blue', key='I2', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='2', enable_events=True, pad=(5,5)), sg.Button('Start 2', enable_events=True, pad=(5,5))],
    [sg.InputText('Lobos', key='I3', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='3', enable_events=True, pad=(5,5)), sg.Button('Start 3', enable_events=True, pad=(5,5))],
    [sg.InputText('Acuâminas', key='I4', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='4', enable_events=True, pad=(5,5)), sg.Button('Start 4', enable_events=True, pad=(5,5))],
    [sg.InputText('Red', key='I5', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='5', enable_events=True, pad=(5,5)), sg.Button('Start 5', enable_events=True, pad=(5,5))],
    [sg.InputText('Krugues', key='I6', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='6', enable_events=True, pad=(5,5)), sg.Button('Start 6', enable_events=True, pad=(5,5))],
    [sg.Text('Red Side')],
    [sg.InputText('Krugues', key='I7', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='7', enable_events=True, pad=(5,5)), sg.Button('Start 7', enable_events=True, pad=(5,5))],
    [sg.InputText('Red', key='I8', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='8', enable_events=True, pad=(5,5)), sg.Button('Start 8', enable_events=True, pad=(5,5))],
    [sg.InputText('Acuâminas', key='I9', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='9', enable_events=True, pad=(5,5)), sg.Button('Start 9', enable_events=True, pad=(5,5))],
    [sg.InputText('Lobos', key='I10', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='10', enable_events=True, pad=(5,5)), sg.Button('Start 10', enable_events=True, pad=(5,5))],
    [sg.InputText('Blue', key='I11', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='11', enable_events=True, pad=(5,5)), sg.Button('Start 11', enable_events=True, pad=(5,5))],
    [sg.InputText('Grompe', key='I12', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='12', enable_events=True, pad=(5,5)), sg.Button('Start 12', enable_events=True, pad=(5,5))],
    [sg.Text('Free Map')],
    [sg.InputText('Barão', key='I13', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='13', enable_events=True, pad=(5,5)), sg.Button('Start 13', enable_events=True, pad=(5,5))],
    [sg.InputText('Arongueijo1', key='I14', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='14', enable_events=True, pad=(5,5)), sg.Button('Start 14', enable_events=True, pad=(5,5))],
    [sg.InputText('Arongueijo2', key='I15', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='15', enable_events=True, pad=(5,5)), sg.Button('Start 15', enable_events=True, pad=(5,5))],
    [sg.InputText('Dragão', key='I16', size=(10,1), pad=(5,5)), sg.Text('Tempo', key='16', enable_events=True, pad=(5,5)), sg.Button('Start 16', enable_events=True, pad=(5,5))],
]

window = sg.Window('Regresser', layout, size=(215,680), margins=(10,10), finalize=True)

# Backend

window['I1'].bind('<Button-1>', '+FOCUS IN+')
window['I2'].bind('<Button>', '+FOCUS IN2+')
window['I3'].bind('<Button>', '+FOCUS IN3+')
window['I4'].bind('<Button>', '+FOCUS IN4+')
window['I5'].bind('<Button>', '+FOCUS IN5+')



while True:
    event, values = window.read(timeout=1000)
    if event == 'Start 1':
        reg('1')
    elif event == 'Start 2':
        reg('2')
    elif event == 'Start 3':
        reg('3')
    elif event == 'Start 4':
        reg('4')
    elif event == 'Start 5':
        reg('5')
    elif event == 'Start 6':
        reg('6')
    elif event == 'Start 7':
        reg('7')
    elif event == 'Start 8':
        reg('8')
    elif event == 'Start 9':
        reg('9')
    elif event == 'Start 10':
        reg('10')
    elif event == 'Start 11':
        reg('11')
    elif event == 'Start 12':
        reg('12')
    elif event == 'Start 13':
        reg('13')
    elif event == 'Start 14':
        reg('14')
    elif event == 'Start 15':
        reg('15')
    elif event == 'Start 16':
        reg('16')

    
    elif event == 'I1+FOCUS IN+':
        window['I1'].update('')
    elif event == 'I2+FOCUS IN2+':
        window['I2'].update('')
    elif event == 'I3+FOCUS IN3+':
        window['I3'].update('')
    elif event == 'I4+FOCUS IN4+':
        window['I4'].update('')
    elif event == 'I5+FOCUS IN5+':
        window['I5'].update('')
    

    elif event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    window.refresh()

window.close()