# Wand & Whisk: Milk Panic

A one-level 2D side-scrolling browser game starring the four Wand & Whisk Cafe mascot girls: Strawberry, Matcha, Ube and Creamia. The cafe owner approved using the characters. The final boss is Strawberry Milk, the cafe's pink-spotted cow mascot.

Cafe website: https://wandandwhiskcafe.com

## Play it

There are three versions, one per branch. Each one is live:

| Version | Branch | Play | What it is |
|---|---|---|---|
| Walking (current work) | [walking](https://github.com/odyssey-jotun/wand-whisk-game/tree/walking) | https://odyssey-jotun.github.io/wand-whisk-game/walking/ | Girls stand and run on legs cut from new full-body art, with drawn poses for crouch, jump, cast and walk where they exist |
| Floating | [animated](https://github.com/odyssey-jotun/wand-whisk-game/tree/animated) | https://odyssey-jotun.github.io/wand-whisk-game/animated/ | Original cafe art, girls hover with squash, stretch and trails |
| Original | [main](https://github.com/odyssey-jotun/wand-whisk-game/tree/main) | https://odyssey-jotun.github.io/wand-whisk-game/ | First version, original cafe art sliding on the ground |

Controls: arrow keys or A/D to move, Down or S to crouch, Space to jump, X to shoot. Hold X to charge a special (costs mana). On phones, on-screen buttons, played sideways.

## How the game works

The whole game is one file: [index.html](https://github.com/odyssey-jotun/wand-whisk-game/blob/walking/index.html). It's plain HTML5 canvas and JavaScript, with no build step and no libraries.

- **Level:** a pastel cafe with crepe platforms, waffle blocks, stars to collect, milk droplet and milk carton enemies, then a boss arena.
- **Boss:** Strawberry Milk the cow ([cow.png](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/assets/cow.png)) hops at the player, sprays milk fountains and spits aimed shots, and speeds up below half health.
- **Potions:** enemies drop the cafe's real Health Float ([image](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/assets/potion-health.png)) and Mana Float ([image](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/assets/potion-mana.png)).
- **Attacks:** tap X for each girl's basic shot. Hold X to charge, then release for her special:

| Girl | Tap | Charged special |
|---|---|---|
| Strawberry | Strawberries | Giant heart that passes through everything |
| Matcha | Rapid matcha bubbles | Fan of eight big bubbles |
| Ube | Stars that curve toward enemies | Three homing moons |
| Creamia | Soft serve lobbed in an arc | Rolling taiyaki |

## How the characters are drawn

Each girl is shown one of two ways, picked per move:

1. **Drawn poses (best):** a whole drawing of the girl in that pose, shown as is. Set up in `POSES` in [index.html](https://github.com/odyssey-jotun/wand-whisk-game/blob/walking/index.html).
2. **Cut-out rig (fallback):** her standing drawing cut into a body piece plus thigh and shin pieces for each leg, which the code swings at the hip and knee. Set up in `RIGS` in [index.html](https://github.com/odyssey-jotun/wand-whisk-game/blob/walking/index.html). The pieces are made by [art-source/cut_rig.py](https://github.com/odyssey-jotun/wand-whisk-game/blob/walking/art-source/cut_rig.py) and live in [assets/rig/](https://github.com/odyssey-jotun/wand-whisk-game/tree/walking/assets/rig).

Drawn poses look far better. The goal is a full set of drawn poses for every girl.

## Character art

Full-size source art, all made in ChatGPT from the cafe's originals, in [art-source/](https://github.com/odyssey-jotun/wand-whisk-game/tree/walking/art-source):

| Girl | Stand | Walk | Jump | Crouch | Cast |
|---|---|---|---|---|---|
| Strawberry | [stand](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/art-source/strawberry-stand.png) | needed | needed | needed | needed |
| Matcha | [stand](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/art-source/matcha-stand.png) | needed | needed | needed | needed |
| Ube | [stand](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/art-source/ube-stand.png) | [walk](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/art-source/ube-walk.png) | [jump](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/art-source/ube-jump.png) | [crouch](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/art-source/ube-crouch.png) | [cast](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/art-source/ube-cast.png) |
| Creamia | [stand](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/art-source/creamia-stand.png) | needed | needed | needed | needed |

Original cafe art the game started from: [Strawberry](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/assets/strawberry.png), [Matcha](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/assets/matcha.png), [Ube](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/assets/ube.png), [Creamia](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/assets/creamia.png), [cafe logo](https://raw.githubusercontent.com/odyssey-jotun/wand-whisk-game/walking/assets/logo.png).

## Art still needed

For each girl, a set of full-body frames, one image per frame:

1. **STAND:** idle, feet planted
2. **WALK 1:** mid-stride, near leg forward
3. **WALK 2:** passing pose, legs together, one foot lifted
4. **WALK 3:** mid-stride, the other leg forward
5. **WALK 4:** passing pose, the other foot lifted
6. **JUMP:** in the air, knees tucked
7. **CROUCH:** squatting low, knees bent
8. **CAST:** front arm straight out at shoulder height, pointing her held item forward (no magic effect drawn)
9. **HURT:** knocked back, eyes shut

Rules for every frame:

- Facing right, three-quarter side view, the same angle in every frame.
- Exactly the same character as the reference: face, hair, outfit, colors, held items, line weight and style. Nothing added, removed or redesigned.
- Same scale in every frame, so she's the same height when standing.
- Full body visible with space around her, nothing cropped.
- Plain pure white background: no shadow, scenery, ground line, text or effects.
- In the four walk frames, the upper body stays nearly identical and only the legs, arm swing, hair and cape move. They play in a loop, so any change in face, size or outfit looks like flickering.

## Files

- [index.html](https://github.com/odyssey-jotun/wand-whisk-game/blob/walking/index.html): the whole game
- [assets/](https://github.com/odyssey-jotun/wand-whisk-game/tree/walking/assets): images the game loads
- [assets/rig/](https://github.com/odyssey-jotun/wand-whisk-game/tree/walking/assets/rig): rig pieces and pose images, at game size
- [art-source/](https://github.com/odyssey-jotun/wand-whisk-game/tree/walking/art-source): full-size art the rig pieces and poses are cut from
- [art-source/cut_rig.py](https://github.com/odyssey-jotun/wand-whisk-game/blob/walking/art-source/cut_rig.py): cuts a standing image into body and leg pieces
- [.github/workflows/deploy.yml](https://github.com/odyssey-jotun/wand-whisk-game/blob/walking/.github/workflows/deploy.yml): publishes all three branches to GitHub Pages
