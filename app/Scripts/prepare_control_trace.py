"""Test trace of the controls scripts read (PG_TEST_CONTROLS=1; see pg_control_read in Source/EngineHost.c).

Wraps the script commands IS_CONTROL_PRESSED, GET_CONTROL_VALUE, GET_CONTROL_NORMAL and their
DISABLED_ forms, the UNBOUND_NORMAL stick reads and the JUST_PRESSED/JUST_RELEASED checks: the original becomes static and a wrapper with the engine's name reports each
answer, so a test can see which inputs a minigame polls and what the touch controls give it
(the yoga poses, GTA-37). Off by default: the host returns at once.
"""
from pathlib import Path
from engine_names import fn
import re
root = Path(__file__).resolve().parents[1]
COMMANDS = [('pad_commands::CommandIsControlPressed(int, int)', 'u32', 0), ('pad_commands::CommandGetControlValue(int, int)', 'u32', 1),
            ('pad_commands::CommandGetControlNormal(int, int)', 'f32', 2), ('pad_commands::CommandIsDisabledControlPressed(int, int)', 'u32', 3),
            ('pad_commands::CommandGetDisabledControlNormal(int, int)', 'f32', 4),
            # Minigames read analog sticks with the unbound forms and buttons with the just-pressed ones
            # (the yoga poses read both sticks this way; GTA-37): they count as polls too.
            ('pad_commands::CommandGetControlUnboundNormal(int, int)', 'f32', 2), ('pad_commands::CommandGetDisabledControlUnboundNormal(int, int)', 'f32', 4),
            ('pad_commands::CommandIsControlJustPressed(int, int)', 'u32', 0), ('pad_commands::CommandIsControlJustReleased(int, int)', 'u32', 0),
            ('pad_commands::CommandIsDisabledControlJustPressed(int, int)', 'u32', 3), ('pad_commands::CommandIsDisabledControlJustReleased(int, int)', 'u32', 3)]
DECLARATION = 'extern void pg_control_read(u32 kind, u32 control, u32 action, f32 value);'

def body_range(s, head):
    start = s.index(head)
    return start, s.index('\n}\n', start) + 3

for name, kind, tag in COMMANDS:
    function = fn(name)
    head = f'{kind} w2c_game_f{function}(w2c_game* instance, u32 var_p0, u32 var_p1) {{'
    path = next(p for p in sorted((root / 'Generated').glob('game_*.c')) if head in p.read_text())
    s = path.read_text()
    if f'pg_control_original_f{function}(' in s: print(f'control trace: f{function} already patched'); continue
    if s.count(head) != 1: raise RuntimeError(f'Pinned f{function} ({name}) changed')
    start, end = body_range(s, head)
    original = s[start:end].replace(head, f'static {kind} pg_control_original_f{function}(w2c_game* instance, u32 var_p0, u32 var_p1) {{', 1)
    wrapper = (f'{head}\n  {kind} value = pg_control_original_f{function}(instance, var_p0, var_p1);\n'
               f'  pg_control_read({tag}, var_p0, var_p1, (f32)value);\n  return value;\n}}\n')
    s = s[:start] + original + wrapper + s[end:]
    if DECLARATION not in s:
        first = re.search(r'^#include "game-[a-z-]*impl\.h"$', s, re.M)
        s = s[:first.end()] + '\n' + DECLARATION + s[first.end():]
    path.write_text(s)
    print(f'control trace: patched f{function} in {path.name}')
