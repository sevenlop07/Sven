import sys
sys.stdout.reconfigure(encoding='utf-8')

setting_path = 'output/com-khong-chan-nuoc-mat/setting.html'
with open(setting_path, 'r', encoding='utf-8') as f:
    s = f.read()

# Replace harmful triggers in setting.html
s = s.replace('vết bầm truyền dịch tím tái', 'miếng băng dán y tế trạm xá')
s = s.replace('vết bầm truyền dịch', 'miếng băng y tế trạm xá')
s = s.replace('vết bầm tím', 'miếng băng dán y tế')
s = s.replace('Duyên ngất xỉu ➔ Má Ba lao tới rơi võng', 'Duyên đuối sức tựa gối ➔ Má Ba nhắc con dâu nghỉ ngơi')
s = s.replace('“Duyên ơi coi chừng té! Khang ơi, đỡ vợ mầy lẹ!”', '“Duyên! Mệt quá thì tựa vô gối nghỉ đi con! Khang, lấy nước ấm cho vợ mau!”')
s = s.replace('“Trời đất ơi... tay mầy bầm dập vầy nè, truyền nước biển hồi nào sao giấu tao?!”', '“Trời đất ơi... cổ tay dán băng y tế nè, đi khám hồi nào sao giấu tao?!”')
s = s.replace('my_duyen jerks her bruised wrist back defensively in Scene 06.', 'my_duyen tucks her bandaged wrist behind her back in Scene 06.')
s = s.replace('vết bầm kim truyền dịch', 'miếng băng dán y tế trạm xá')

with open(setting_path, 'w', encoding='utf-8') as f:
    f.write(s)

print("Purged harmful content triggers from setting.html!")
