import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Scene 01
    (
        'Anh ơi... em đuối sức dữ lắm rồi nè, sữa hổng chịu về giọt nào hết trơn...',
        'Anh ơi... em đuối sức quá chừng rồi, sữa hổng chịu về...'
    ),
    # Scene 02 - Má Ba
    (
        'Trời đất ơi! Thằng Tin khóc thấu trời... mầy nuôi cháu tao cái kiểu gì vậy hả?!',
        'Trời đất ơi! Thằng Tin khóc thấu trời... nuôi cháu tao kiểu gì vậy?!'
    ),
    # Scene 02 - Minh Khang
    (
        'Má ơi con xin má nhỏ tiếng giùm... Duyên thức trắng ba đêm đuối sức lắm má!',
        'Con xin má nhỏ tiếng giùm... Duyên thức trắng ba đêm đuối lắm rồi má!'
    ),
    # Scene 03 - Má Ba
    (
        'Trời ơi cái võng này ba mầy đưa từ đỏ hỏn, giờ mầy chê bỏ xó hả?!',
        'Cái võng này ba mầy đưa từ đỏ hỏn, giờ tụi bây bỏ xó hả?!'
    ),
    # Scene 03 - Minh Khang
    (
        'Má ơi, xương sống con nít còn non xèo... nằm nôi phẳng mới êm dịu má ơi!',
        'Xương sống thằng Tin còn non xèo... nằm nôi phẳng mới êm dịu má ơi!'
    ),
    # Scene 04 - Má Ba
    (
        'Trời đất ơi Duyên! Con làm sao vậy nè?! Khang ơi, vô đỡ vợ mầy lẹ lên!',
        'Chết chưa Duyên ơi! Con làm sao vậy nè?! Khang ơi, đỡ vợ mầy lẹ!'
    ),
    # Scene 05 - Má Ba
    (
        'Trời đất ơi... tay mầy vầy nè, mầy truyền nước biển hồi nào sao giấu tao hả?!',
        'Ủa giấu cái gì... tay mầy vầy nè, truyền nước biển hồi nào sao giấu tao?!'
    ),
    # Scene 06 - Mỹ Duyên
    (
        'Má ơi, con tự ráng được mà má... má bận lòng làm chi thêm nữa má ơi...',
        'Dạ con tự ráng được mà má... má bận lòng làm chi thêm nữa nè...'
    ),
    # Scene 06 - Má Ba
    (
        'Mèn đéc ơi mầy nói cái giọng đó... mầy coi tao như người dưng nước lã hả?!',
        'Mèn đéc ơi... mầy coi tao như người dưng nước lã thiệt rồi hả?!'
    ),
    # Scene 07 - Má Ba
    (
        'Trời ơi tao lặn lội lên đây... đâu phải để tụi bây xua đuổi tao hả trời?!',
        'Trời ơi tao lặn lội lên đây... đâu phải để tụi bây xua đuổi tao?!'
    ),
    # Scene 07 - Minh Khang
    (
        'Má ơi con lạy má! Duyên đuối sức dữ lắm rồi, má nói vậy tội nghiệp nó má!',
        'Con lạy má luôn đó! Duyên đuối sức lắm, má nói vậy tội nghiệp nó má!'
    ),
    # Scene 08 - Má Ba
    (
        'Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao cho biết!',
        'Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao!'
    ),
    # Scene 09 - Mỹ Duyên
    (
        'Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này anh...',
        'Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này...'
    ),
    # Scene 10 - Dì Tám
    (
        'Bà Ba ơi! Con dâu nó leo tuốt lên đầu ngồi, bà nhịn cho đặng hả trời?!',
        'Bà Ba ơi! Con dâu leo tuốt lên đầu ngồi, bà nhịn cho đặng hả?!'
    ),
    # Scene 10 - Má Ba
    (
        'Chị Tám ơi... chị vô coi giùm thằng nhỏ, chớ tui bải hoải tay chân hết trơn rồi...',
        'Chị Tám ơi... vô coi giùm thằng nhỏ, chớ tui bải hoải tay chân hết trơn...'
    ),
]

for old_q, new_q in replacements:
    count = content.count(old_q)
    if count > 0:
        content = content.replace(old_q, new_q)
        print(f"REPLACED ({count}x): '{old_q[:30]}...' -> '{new_q[:30]}...'")
    else:
        print(f"NOT FOUND: '{old_q}'")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nSuccessfully updated tap-1.html with definitive emotional dialogue!")
