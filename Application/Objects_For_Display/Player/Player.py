
from Application.Default_Object.DefaultObjectInformationForPlayer import DefaultInformation
from Application.Default_Object.Character_Movement import CharacterMovement
from Application.Default_Object.MovementKeybinds import MovementKeybinds
class Player(DefaultInformation, CharacterMovement,MovementKeybinds):
    def __init__(self):
        DefaultInformation.__init__(self)
        CharacterMovement.__init__(self)
        MovementKeybinds.__init__(self)