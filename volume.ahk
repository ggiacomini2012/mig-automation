#Requires AutoHotkey v2.0

!F12:: {
    SoundSetVolume(SoundGetVolume() + 1)
}

!F11:: {
    SoundSetVolume(SoundGetVolume() - 1)
}
