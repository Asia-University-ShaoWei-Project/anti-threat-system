class Button:
  def __init__(self, input_pin, output_pin):
    self.In = input_pin
    self.Out = output_pin
    GPIO.setup(input_pin, GPIO.IN)
    GPIO.setup(output_pin, GPIO.OUT)

  def Is_Click(self):
    if GPIO.input(self.In) == 1:
      return True
