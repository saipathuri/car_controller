left_stick_x_index=0
left_stick_y_index=1
trigger_index=2
right_stick_x_index=3
right_stick_y_index=4

stick_threshold=.1
trigger_threshold=.001
def process_axes(socket_client, joystick):
    left_stick_x = joystick.get_axis(left_stick_x_index)
    left_stick_y = joystick.get_axis(left_stick_y_index)
    triggers = joystick.get_axis(trigger_index)
    right_stick_x = joystick.get_axis(right_stick_x_index)
    right_stick_y = joystick.get_axis(right_stick_y_index)

    process_left_stick_x(socket_client, left_stick_x)
    process_triggers(socket_client, triggers)

def process_left_stick_x(socket_client, left_stick_x):
    max_turn = 250
    middle = max_turn/2
    bottom_limit = 40
    if(left_stick_x > stick_threshold):
        turn_amount = (middle*left_stick_x)+middle
        print(f"Turn right: {turn_amount}")
        socket_client.send_action('turn', turn_amount)
    elif (left_stick_x < stick_threshold*-1):
        turn_amount = middle - (middle*left_stick_x*-1)
        if(turn_amount < bottom_limit):
            turn_amount = bottom_limit
        print(f"Turn left: {turn_amount}")
        socket_client.send_action('turn', turn_amount)
    else:
        # print("Turn home")
        socket_client.send_action('turn_home', 0)

def process_triggers(socket_client, triggers):
    min_speed=30
    max_speed=100
    if(triggers > trigger_threshold):
        speed = triggers*max_speed
        if(speed < min_speed):
            speed = min_speed
        print(f"Go backwards: {speed}")
        socket_client.send_action('backward', speed)
    elif(triggers < trigger_threshold*-1):
        speed = triggers*max_speed*-1
        if(speed < min_speed):
            speed = min_speed
        print(f"Go forwards: {speed}")
        socket_client.send_action('forward', speed)
    else:
        # print("Stop")
        socket_client.send_action('motor_stop', 0)