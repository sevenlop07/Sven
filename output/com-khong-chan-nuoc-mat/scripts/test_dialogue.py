import sys
import re
sys.stdout.reconfigure(encoding='utf-8')

lines = [
    ('s01', 'Mỹ Duyên', 'Anh ơi... em đuối sức quá chừng rồi, sữa hổng chịu về...'),
    ('s02', 'Má Ba', 'Trời đất ơi! Thằng Tin khóc thấu trời... nuôi cháu tao kiểu gì vậy?!'),
    ('s02', 'Minh Khang', 'Con xin má nhỏ tiếng giùm... Duyên thức trắng ba đêm đuối lắm rồi má!'),
    ('s03', 'Má Ba', 'Cái võng này ba mầy đưa từ đỏ hỏn, giờ tụi bây bỏ xó hả?!'),
    ('s03', 'Minh Khang', 'Xương sống thằng Tin còn non xèo... nằm nôi phẳng mới êm dịu má ơi!'),
    ('s04', 'Má Ba', 'Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mầy mau!'),
    ('s05', 'Má Ba', 'Trời đất ơi... cổ tay còn dán băng y tế nè, đi khám hồi nào sao giấu tao hả?!'),
    ('s06', 'Mỹ Duyên', 'Dạ con tự ráng được mà má... má bận lòng làm chi thêm nữa nè...'),
    ('s06', 'Má Ba', 'Mèn đéc ơi... mầy coi tao như người dưng nước lã thiệt rồi hả?!'),
    ('s07', 'Má Ba', 'Trời ơi tao lặn lội lên đây... đâu phải để tụi bây xua đuổi tao?!'),
    ('s07', 'Minh Khang', 'Con lạy má luôn đó! Duyên đuối sức lắm, má nói vậy tội nghiệp nó má!'),
    ('s08', 'Má Ba', 'Ờ... tụi bây khôn lớn hết trơn rồi! Để coi tụi bây nuôi con ra sao!'),
    ('s09', 'Mỹ Duyên', 'Anh Khang ơi... em đuối tới chịu hết nổi rồi, nhà mình sao ra nông nỗi này...'),
    ('s10', 'Dì Tám', 'Bà Ba ơi! Con dâu leo tuốt lên đầu ngồi, bà nhịn cho đặng hả?!'),
    ('s10', 'Má Ba', 'Chị Tám ơi... vô coi giùm thằng nhỏ, chớ tui bải hoải tay chân hết trơn...'),
]

banned_emotions = ['ghét', 'thương', 'buồn', 'sợ', 'giận', 'tủi thân', 'hạnh phúc', 'cô đơn', 'đau lòng', 'hối hận', 'xin lỗi', 'đội ơn', 'biết ơn', 'tha thứ', 'nhớ thương']

openers = {}
for sc, spk, text in lines:
    words = text.split()
    wc = len(words)
    emo_hits = [e for e in banned_emotions if re.search(r'(?<!\w)' + re.escape(e) + r'(?!\w)', text.lower())]
    first_two = ' '.join(words[:2]).lower().strip('!,.:?')
    openers[first_two] = openers.get(first_two, 0) + 1
    status = 'OK' if wc <= 18 and not emo_hits else 'FAIL'
    print(f'[{status}] {sc} {spk} ({wc} words): {text}')

print('\nOpeners check:')
for op, cnt in openers.items():
    if cnt >= 2:
        print(f'  Repeat opener: "{op}" x{cnt}')
