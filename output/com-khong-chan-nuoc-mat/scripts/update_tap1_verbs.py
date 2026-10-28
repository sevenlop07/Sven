import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

file_path = 'output/com-khong-chan-nuoc-mat/tap-1.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    # Scene 1
    (
        r'my_duyen:\s*“\s*Anh ơi\.\.\. em đuối sức quá chừng rồi, sữa hổng chịu về\.\.\.\s*”',
        'my_duyen whispers : “ Anh ơi... em đuối sức quá chừng rồi, sữa hổng chịu về... ”'
    ),
    # Scene 2
    (
        r'ma_ba:\s*“\s*Trời đất ơi! Thằng Tin khóc thấu trời\.\.\. nuôi cháu tao kiểu gì vậy\?!\s*”',
        'ma_ba snaps : “ Trời đất ơi! Thằng Tin khóc thấu trời... nuôi cháu tao kiểu gì vậy?! ”'
    ),
    (
        r'minh_khang:\s*“\s*Con xin má nhỏ tiếng giùm\.\.\. Duyên thức trắng ba đêm đuối lắm rồi má!\s*”',
        'minh_khang replies : “ Con xin má nhỏ tiếng giùm... Duyên thức trắng ba đêm đuối lắm rồi má! ”'
    ),
    # Scene 3
    (
        r'ma_ba:\s*“\s*Cái võng này ba mầy đưa từ đỏ hỏn, giờ tụi bây bỏ xó hả\?!\s*”',
        'ma_ba snaps : “ Cái võng này ba mầy đưa từ đỏ hỏn, giờ tụi bây bỏ xó hả?! ”'
    ),
    (
        r'minh_khang:\s*“\s*Xương sống thằng Tin non xèo\.\.\. nằm nôi phẳng mới êm dịu má!\s*”',
        'minh_khang replies : “ Xương sống thằng Tin non xèo... nằm nôi phẳng mới êm dịu má! ”'
    ),
    # Scene 4
    (
        r'ma_ba:\s*“\s*Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau!\s*”',
        'ma_ba says : “ Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau! ”'
    ),
    # Scene 5
    (
        r'ma_ba:\s*“\s*Trời đất ơi\.\.\. cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao\?!\s*”',
        'ma_ba says : “ Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?! ”'
    ),
    # Scene 6
    (
        r'my_duyen:\s*“\s*Dạ con tự ráng được mà má\.\.\. má bận lòng làm chi thêm nữa nè\.\.\.\s*”',
        'my_duyen says : “ Dạ con tự ráng được mà má... má bận lòng làm chi thêm nữa nè... ”'
    ),
    (
        r'ma_ba:\s*“\s*Mèn đéc ơi\.\.\. mầy coi tao như người dưng nước lã thiệt rồi hả\?!\s*”',
        'ma_ba replies : “ Mèn đéc ơi... mầy coi tao như người dưng nước lã thiệt rồi hả?! ”'
    ),
    # Scene 7
    (
        r'ma_ba:\s*“\s*Trời ơi tao lặn lội lên đây\.\.\. đâu phải để tụi bây xua đuổi tao\?!\s*”',
        'ma_ba snaps : “ Trời ơi tao lặn lội lên đây... đâu phải để tụi bây xua đuổi tao?! ”'
    ),
    (
        r'minh_khang:\s*“\s*Con lạy má luôn đó! Duyên đuối sức lắm, má nói vậy tội nghiệp nó má!\s*”',
        'minh_khang replies : “ Con lạy má luôn đó! Duyên đuối sức lắm, má nói vậy tội nghiệp nó má! ”'
    ),
    # Scene 8
    (
        r'ma_ba:\s*“\s*Ờ\.\.\. tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao!\s*”',
        'ma_ba snaps : “ Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao! ”'
    ),
    # Scene 9
    (
        r'my_duyen:\s*“\s*Anh Khang ơi\.\.\. em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này\.\.\.\s*”',
        'my_duyen whispers : “ Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này... ”'
    ),
    # Scene 10
    (
        r'di_tam:\s*“\s*Bà Ba ơi! Con dâu leo tuốt lên đầu ngồi, bà nhịn cho đặng hả\?!\s*”',
        'di_tam snaps : “ Bà Ba ơi! Con dâu leo tuốt lên đầu ngồi, bà nhịn cho đặng hả?! ”'
    ),
    (
        r'ma_ba:\s*“\s*Chị Tám ơi\.\.\. vô coi giùm thằng nhỏ, chớ tui bải hoải tay chân hết trơn\.\.\.\s*”',
        'ma_ba replies : “ Chị Tám ơi... vô coi giùm thằng nhỏ, chớ tui bải hoải tay chân hết trơn... ”'
    ),
]

count = 0
for pattern, repl in replacements:
    content, n = re.subn(pattern, repl, content)
    count += n
    if n == 0:
        print(f"Warning: pattern not matched: {pattern}")

print(f"Total replacements made: {count}/15")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Saved tap-1.html successfully.")
