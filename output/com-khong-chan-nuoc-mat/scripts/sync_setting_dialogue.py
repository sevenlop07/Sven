import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

file_path = 'output/com-khong-chan-nuoc-mat/setting.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Scene 01
    (
        'Anh ơi... em kiệt sức rồi, sữa hổng chịu về...',
        'Anh ơi... em đuối sức quá chừng rồi, sữa hổng chịu về...'
    ),
    # Scene 02 - Má Ba
    (
        'Trời đất! Thằng Tin khóc thấu trời... nuôi cháu tao kiểu Tây hả?!',
        'Trời đất ơi! Thằng Tin khóc thấu trời... nuôi cháu tao kiểu gì vậy?!'
    ),
    # Scene 02 - Minh Khang
    (
        'Má nhỏ tiếng giùm con... Duyên kiệt sức ba đêm rồi!',
        'Con xin má nhỏ tiếng giùm... Duyên thức trắng ba đêm đuối lắm rồi má!'
    ),
    # Scene 03 - Má Ba
    (
        'Cái võng này ba bây đưa bây ngủ từ hồi đỏ hỏn đó!',
        'Cái võng này ba mầy đưa từ đỏ hỏn, giờ tụi bây bỏ xó hả?!'
    ),
    # Scene 03 - Minh Khang
    (
        'Con nhớ võng của ba... mà thằng Tin phải nằm nôi.',
        'Xương sống thằng Tin non xèo... nằm nôi phẳng mới êm dịu má!'
    ),
    # Scene 04 - Má Ba
    (
        'Duyên! Duyên ơi, con sao vậy con?! Khang, đỡ vợ mầy mau!',
        'Chết chưa Duyên ơi! Con làm sao vậy nè?! Khang ơi, đỡ vợ mầy lẹ!'
    ),
    # Scene 05 - Má Ba
    (
        'Tay mầy... mầy đi truyền nước biển hồi nào sao hổng nói tao hay?!',
        'Ủa giấu cái gì... tay mầy vầy nè, truyền nước biển hồi nào sao giấu tao?!'
    ),
    # Scene 06 - Mỹ Duyên
    (
        'Con tự lo được... má đừng bận lòng thêm...',
        'Dạ con tự ráng được mà má... má bận lòng làm chi thêm nữa nè...'
    ),
    # Scene 06 - Má Ba
    (
        'Mầy nói vậy... là mầy coi tao là người dưng nước lã?!',
        'Mèn đéc ơi... mầy coi tao như người dưng nước lã thiệt rồi hả?!'
    ),
    # Scene 07 - Má Ba
    (
        'Tao lặn lội lên đây... hổng phải để tụi bây xua đuổi!',
        'Trời ơi tao lặn lội lên đây... đâu phải để tụi bây xua đuổi tao?!'
    ),
    # Scene 07 - Minh Khang
    (
        'Má! Duyên nó đang bệnh, má đừng nói vậy tội nghiệp nó!',
        'Con lạy má luôn đó! Duyên đuối sức lắm, má nói vậy tội nghiệp nó má!'
    ),
    # Scene 08 - Má Ba
    (
        'Được rồi... tụi bây khôn rồi, để coi tụi bây nuôi con ra sao!',
        'Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao!'
    ),
    # Scene 09 - Mỹ Duyên
    (
        'Em mệt quá Khang ơi... nhà mình hổng thở nổi nữa rồi...',
        'Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này...'
    ),
    # Scene 10 - Dì Tám
    (
        'Bà Ba! Con dâu nó leo lên đầu ngồi mà bà nhịn hả?!',
        'Bà Ba ơi! Con dâu leo tuốt lên đầu ngồi, bà nhịn cho đặng hả?!'
    ),
    # Scene 10 - Má Ba
    (
        'Chị Tám... chị vô đây coi cháu tao giùm tao!',
        'Chị Tám ơi... vô coi giùm thằng nhỏ, chớ tui bải hoải tay chân hết trơn...'
    ),
]

for old_q, new_q in replacements:
    count = content.count(old_q)
    if count > 0:
        content = content.replace(old_q, new_q)
        print(f"REPLACED ({count}x) in setting.html: '{old_q[:30]}...' -> '{new_q[:30]}...'")
    else:
        print(f"NOT FOUND: '{old_q}'")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nSuccessfully synchronized setting.html with definitive dialogue!")
