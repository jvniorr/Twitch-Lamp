import time
import questionary
import serial_ports
import edit_list
import config
import twitchapi
import serial
import time


def menu():
    menu = questionary.select('What do you want to do?',
                              choices=['Start', 'Show the streamers list',
                                       'Delete a streamer from the list', 'Add a streamer to the list'],
                              default='Start'
                              ).ask()
    return menu


serial_port = serial_ports.select_serial_port()

while serial_port == 'Refresh':
    serial_port = serial_ports.select_serial_port()

arduino = serial.Serial(serial_port, 9600)


def get_streamer_status(streamer):
    request = twitchapi.request_json(streamer)
    if request['data'] == []:
        pass
    else:
        get_color_and_send(streamer)
    time.sleep(4)


def get_color_and_send(streamer):
    dic = edit_list.read_file()
    color = dic[streamer]
    arduino.write(str.encode(color[0]))


while True:
    selected = menu()
    if selected == 'Show the streamers list':
        questionary.select(edit_list.dict_keys_to_list(),
                           choices=['Back']).ask()
    elif selected == 'Delete a streamer from the list':
        delete_nick = questionary.select(
            'Who do you want to delete?', choices=edit_list.dictionary_with_back()).ask()
        if delete_nick == 'Back':
            pass
        else:
            edit_list.delete_element(delete_nick)
    elif selected == 'Add a streamer to the list':
        nickname = questionary.text(
            "Enter streamer's twitch.tv nickname").ask()
        color = questionary.select(
            'Choose a color of the lamp that will be on, when the streamer is online', choices=config.colors).ask()
        edit_list.add_element(nickname, color)

    while selected == 'Start':
        for streamer in edit_list.read_file():
            get_streamer_status(streamer)
