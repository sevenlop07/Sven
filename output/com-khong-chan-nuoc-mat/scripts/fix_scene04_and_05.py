import sys
sys.stdout.reconfigure(encoding='utf-8')

def update_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Scene 04 fix
    old_s04 = "Chết chưa Duyên ơi! Con làm sao vậy nè?! Khang ơi, đỡ vợ mầy lẹ!"
    new_s04 = "Duyên ơi coi chừng té! Khang ơi, vô đỡ vợ mầy lẹ lên con!"

    # Scene 05 fix
    old_s05 = "Ủa giấu cái gì... tay mầy vầy nè, truyền nước biển hồi nào sao giấu tao?!"
    new_s05 = "Trời đất ơi... tay mầy bầm dập vầy nè, truyền nước biển hồi nào sao giấu tao?!"

    count_s04 = content.count(old_s04)
    count_s05 = content.count(old_s05)

    content = content.replace(old_s04, new_s04)
    content = content.replace(old_s05, new_s05)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {file_path}: s04 replaced {count_s04}x, s05 replaced {count_s05}x")

update_file('output/com-khong-chan-nuoc-mat/tap-1.html')
update_file('output/com-khong-chan-nuoc-mat/setting.html')
