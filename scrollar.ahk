#Requires AutoHotkey v2.0

global Scrolling := false

; Quando pressiona o botão do meio (rodinha do mouse)
MButton:: {
    global Scrolling := true
    while (Scrolling) {
        MouseGetPos &x, &y
        Sleep 10
        MouseGetPos &newX, &newY
        deltaY := newY - y
        if (Abs(deltaY) > 2) { ; Se o movimento for maior que 2 pixels
            if (deltaY > 0) {
                Send("{WheelDown}") ; Scroll para baixo
            } else {
                Send("{WheelUp}") ; Scroll para cima
            }
        }
        x := newX
        y := newY
    }
}

; Quando solta o botão do meio, para o scroll
MButton Up:: {
    global Scrolling := false
}
