# Mods

The app loads PC mods for GTA V as they are downloaded (from gta5-mods.com, for example). You don't convert anything: install them from **Settings › Mods**, or put the files in the app's **Mods** folder yourself, using the same folder names as on PC.

**Mods can break the game.** Crashes, missing textures or odd behaviour caused by a mod are not bugs in the port, and we can't fix other people's mods. Ask about mods in the **Mods** topic on Telegram. Please send logs (Settings › This device › Send log to the developer) only for problems that also happen with the Mods folder empty. Logs show which mods were active.

## What works

| Kind of mod | Works | Notes |
|---|---|---|
| Replace a car, bike or plane | Yes | `.yft` / `.ytd` files inside `vehicles.rpf` |
| Replace a character or skin | Yes | `.ydd` / `.yft` / `.ytd` / `.ymt` inside the ped archives |
| Add-on cars (`dlc.rpf` packs) | Yes | Added to the game's pack list automatically |
| OpenIV packages (`.oiv`) | Yes | Drop the `.oiv` file (or its unpacked folder) into Mods |
| Data files (handling, AI, weather...) | Yes | Whole-file replacements, e.g. `vehicleaihandlinginfo.meta` |
| Script Hook V scripts (`.asi`), trainers | Yes | Simple Trainer and similar; see [Scripts](#scripts-asi) |
| ScriptHookVDotNet scripts (C# `.dll` in a `scripts` folder) | No | Not supported |
| ASI files that patch the PC game (packfile or heap limit adjusters, OpenIV.asi, gameconfig fixes) | Not needed | The port handles those limits itself. They load but do nothing |
| Replacing files inside an archive that is inside another archive (for example a car in a DLC pack's `vehicles.rpf`) | Not yet | The log says which file was skipped |
| Adding a brand-new file to one of the game's archives | Not yet | Replacing existing files works. Add-on packs bring their own archive and work |

This is the PC game at the version the port is built from. Mods made for newer GTA updates can refer to cars, clothes or game commands this version doesn't have. Those parts won't show up, and the log names them.

## Installing a mod (the easy way)

1. Download the mod on your iPhone (Safari saves it to Files › Downloads).
2. In the app: **Settings › Mods › Install a mod…** and pick the file as you downloaded it: `.zip`, `.rar`, `.oiv`, `.asi` or loose files. (`.7z` isn't supported yet: unpack it first.)
3. The app works out where each file goes and shows you before installing: which game file each one replaces, which add-on pack it adds, and what it leaves out and why.
4. Start the game.

Each mod gets its own folder in Mods. **Settings › Mods** lists them: switch a mod off or on, or swipe to remove it.

The app knows where files go because the game itself does: while the game runs, it records where every file lives in its archives. So **start the game once before installing loose car or skin files**. Mods that come in their game folders, add-ons, `.oiv` and `.asi` files don't need that.

Some things the app won't guess, so it leaves them out and says so:
- a settings file (`vehicles.meta`, `carcols.meta`...) that the game has in several places, when the readme doesn't name one;
- a car's settings when its model can't be installed;
- PC limit files (`gameconfig.xml` and similar), which aren't needed here and would break the game.

Put those in by hand if you know where they go (below).

## Before you start

- Cars, skins and add-on packs need the **game files on your iPhone**: tap **Game files** and choose **A folder on this iPhone**. When the game streams from a server, only whole-file mods (data files, scripts) load.
- The Mods folder is in the Files app: **On My iPhone › GTA V Port › Mods**. It appears after the first launch. A `README.txt` inside it has a short version of this page.
- Mods are read when the game starts. After adding or removing mods, close the game completely and start it again.

## Putting files in by hand

Use the path the mod's readme gives for OpenIV, starting from the game folder. Upper or lower case doesn't matter. The `mods/` folder that OpenIV uses is not needed here; if your copy has it, that works too.

**Replace a car** (Nissan Altima replacing the Ubermacht Oracle):

```
Mods/x64e.rpf/levels/gta5/vehicles.rpf/oracle.yft
Mods/x64e.rpf/levels/gta5/vehicles.rpf/oracle_hi.yft
Mods/x64e.rpf/levels/gta5/vehicles.rpf/oracle.ytd
```

On PC the vehicle archive is in `x64e.rpf`. Some readmes say `x64e.rpf\levels\gta5\vehicles.rpf\`, others only `vehicles.rpf`; use the full path above.

**Replace a character** (an ambient biker):

```
Mods/x64v.rpf/models/cdimages/componentpeds_g_m_y.rpf/g_m_y_lost_01.ydd
Mods/x64v.rpf/models/cdimages/componentpeds_g_m_y.rpf/g_m_y_lost_01.ytd
...
```

Main characters are in `x64v.rpf/models/cdimages/streamedpeds_players.rpf/player_zero/` (Michael), `player_one/` (Franklin) and `player_two/` (Trevor).

**Add-on car** (a mod with its own `dlc.rpf`):

```
Mods/update/x64/dlcpacks/a80/dlc.rpf
```

Skip the step where the readme asks you to edit `dlclist.xml`: the app adds every pack it finds to the list. The car's spawn name is in the mod's readme. Spawn it with a trainer.

**OpenIV package** (`.oiv`): put the file in Mods as it is, for example `Mods/Lamborghini Veneno.oiv`. An unpacked package (a folder with `assembly.xml` and `content/`) works too. The app installs it the way OpenIV would, including the edits it makes to game files.

**Data file** (Faster AI Drivers):

```
Mods/common.rpf/data/ai/vehicleaihandlinginfo.meta
```

Paths under `update/update.rpf/common/...` work as well.

## Scripts (`.asi`)

Script Hook V scripts are Windows files. The app runs them in a built-in interpreter, so the same `.asi` file from gta5-mods.com works.

- Put the `.asi` file and its settings (`.ini`) at the top of the Mods folder, for example `Mods/TrainerV.asi` and `Mods/trainerv.ini`.
- You don't need `ScriptHookV.dll`, `dinput8.dll` or an ASI loader. If they're in the folder, they're ignored.
- **Keys:** PC scripts use the keyboard (Simple Trainer opens with F3). While a script mod runs, a **Mod keys** button appears at the top of the screen. It opens a keypad with exactly the keys your mods use. Hold a key to press it. A long press pins the key next to the button, so the key that opens your trainer is one tap away. Shift, Ctrl and Alt stay down after a tap until you press the next key, for combinations like Alt + A.
- **Typing:** when a script asks for text (spawn a car by name, a search box), the iPhone keyboard opens with the script's question. Type and tap OK; the script gets the text.
- Controller shortcuts work through the touch controls and Bluetooth controllers too (Simple Trainer: RB + X opens the menu, D-pad and A/B to move around). A keyboard connected to an iPad works as well.
- Features that change the PC game's memory directly (some trainer options) stay off. The rest of the script keeps working.
- A script that crashes or freezes is stopped on its own. The game keeps running, and the log says what happened.
- Scripts cost a little speed: Simple Trainer takes about 2 to 3 ms per frame.

## Removing mods

In **Settings › Mods**, swipe a mod to remove it or switch it off. Files you put in by hand: delete them from the Mods folder. Start the game again afterwards. The game's own files are never changed.

## Something isn't working

1. Check the log (Settings › This device › Send log to the developer). Every mod file is listed with what happened to it. "Mods: ... ignored" lines say why a file wasn't used.
2. Try the mod alone, with nothing else in the Mods folder.
3. Ask in the **Mods** topic on Telegram, with the mod's name and link.
