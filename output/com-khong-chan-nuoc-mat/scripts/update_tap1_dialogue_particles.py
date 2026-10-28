import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replacements: (old_dialogue_quote, new_dialogue_quote)
dialogue_updates = [
    # Scene 01
    (
        'Anh ơi... em kiệt sức rồi, sữa hổng chịu về...',
        'Anh ơi... em đuối sức dữ lắm rồi nè, sữa hổng chịu về giọt nào hết trơn...'
    ),
    # Scene 02 - Má Ba
    (
        'Trời đất! Thằng Tin khóc thấu trời... nuôi cháu tao kiểu Tây hả?!',
        'Trời đất ơi! Thằng Tin khóc thấu trời... mầy nuôi cháu tao cái kiểu gì vậy hả?!'
    ),
    # Scene 02 - Minh Khang
    (
        'Má nhỏ tiếng giùm con... Duyên kiệt sức ba đêm rồi!',
        'Má ơi con xin má nhỏ tiếng giùm... Duyên thức trắng ba đêm đuối sức lắm má!'
    ),
    # Scene 03 - Má Ba
    (
        'Cái võng này ba bây đưa bây ngủ từ hồi đỏ hỏn đó!',
        'Trời ơi cái võng này ba mầy đưa từ đỏ hỏn, giờ mầy chê bỏ xó hả?!'
    ),
    # Scene 03 - Minh Khang
    (
        'Con nhớ võng của ba... mà thằng Tin phải nằm nôi.',
        'Má ơi, xương sống con nít còn non xèo... nằm nôi phẳng mới êm dịu má ơi!'
    ),
    # Scene 04 - Má Ba
    (
        'Duyên! Duyên ơi, con sao vậy con?! Khang, đỡ vợ mầy mau!',
        'Trời đất ơi Duyên! Con làm sao vậy nè?! Khang ơi, vô đỡ vợ mầy lẹ lên!'
    ),
    # Scene 05 - Má Ba
    (
        'Tay mầy... mầy đi truyền nước biển hồi nào sao hổng nói tao hay?!',
        'Trời đất ơi... tay mầy vầy nè, mầy truyền nước biển hồi nào sao giấu tao hả?!'
    ),
    # Scene 06 - Mỹ Duyên
    (
        'Con tự lo được... má đừng bận lòng thêm...',
        'Má ơi, con tự ráng được mà má... má bận lòng làm chi thêm nữa má ơi...'
    ),
    # Scene 06 - Má Ba
    (
        'Mầy nói vậy... là mầy coi tao là người dưng nước lã?!',
        'Mèn đéc ơi mầy nói cái giọng đó... mầy coi tao như người dưng nước lã hả?!'
    ),
    # Scene 07 - Má Ba
    (
        'Tao lặn lội lên đây... hổng phải để tụi bây xua đuổi!',
        'Trời ơi tao lặn lội lên đây... đâu phải để tụi bây xua đuổi tao hả trời?!'
    ),
    # Scene 07 - Minh Khang
    (
        'Má! Duyên nó đang bệnh, má đừng nói vậy tội nghiệp nó!',
        'Má ơi con lạy má! Duyên đuối sức dữ lắm rồi, má nói vậy tội nghiệp nó má!'
    ),
    # Scene 08 - Má Ba
    (
        'Được rồi... tụi bây khôn rồi, để coi tụi bây nuôi con ra sao!',
        'Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao cho biết!'
    ),
    # Scene 09 - Mỹ Duyên
    (
        'Em mệt quá Khang ơi... nhà mình hổng thở nổi nữa rồi...',
        'Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này anh...'
    ),
    # Scene 10 - Dì Tám
    (
        'Bà Ba! Con dâu nó leo lên đầu ngồi mà bà nhịn hả?!',
        'Bà Ba ơi! Con dâu nó leo tuốt lên đầu ngồi, bà nhịn cho đặng hả trời?!'
    ),
    # Scene 10 - Má Ba
    (
        'Chị Tám... chị vô đây coi cháu tao giùm tao!',
        'Chị Tám ơi... chị vô coi giùm thằng nhỏ, chớ tui bải hoải tay chân hết trơn rồi...'
    ),
]

for old_q, new_q in dialogue_updates:
    if old_q in content:
        content = content.replace(old_q, new_q)
        print(f"REPLACED: {old_q[:35]}... -> {new_q[:35]}...")
    else:
        print(f"NOT FOUND: {old_q}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nSuccessfully updated all dialogue in tap-1.html!")
