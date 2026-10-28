import re
import os
import sys

if sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

tap1_path = r"output/com-khong-chan-nuoc-mat/tap-1.html"
with open(tap1_path, "r", encoding="utf-8") as f:
    text = f.read()

replacements = [
    # Scene 02
    (
        '"Trời đất ơi! Bát cháo nguội ngắt... con nít ba tuần để đói hả?!"',
        '"Trời đất ơi! Cháo nguội ngắt... con nít để đói hả?!"'
    ),
    (
        '"Má nhỏ tiếng giùm con... Duyên thức trắng ba đêm kiệt sức rồi!"',
        '"Má nhỏ tiếng giùm... Duyên thức ba đêm kiệt sức rồi!"'
    ),
    (
        '“ Trời đất ơi! Bát cháo nguội ngắt... con nít ba tuần để đói hả?! ”',
        '“ Trời đất ơi! Cháo nguội ngắt... con nít để đói hả?! ”'
    ),
    (
        '“ Má nhỏ tiếng giùm con... Duyên thức trắng ba đêm kiệt sức rồi! ”',
        '“ Má nhỏ tiếng giùm... Duyên thức ba đêm kiệt sức rồi! ”'
    ),

    # Scene 03
    (
        '"Cái võng ba mầy đưa từ nhỏ, đem cháu tao bỏ xó nôi hả?!"',
        '"Võng ba mầy đưa, đem cháu tao bỏ xó nôi hả?!"'
    ),
    (
        '"Cột sống thằng Tin non xèo... bác sĩ dặn nằm nôi phẳng má ơi!"',
        '"Thằng Tin xương non xèo... bác sĩ dặn nằm nôi phẳng má!"'
    ),
    (
        '“ Cái võng ba mầy đưa từ nhỏ, đem cháu tao bỏ xó nôi hả?! ”',
        '“ Võng ba mầy đưa, đem cháu tao bỏ xó nôi hả?! ”'
    ),
    (
        '“ Cột sống thằng Tin non xèo... bác sĩ dặn nằm nôi phẳng má ơi! ”',
        '“ Thằng Tin xương non xèo... bác sĩ dặn nằm nôi phẳng má! ”'
    ),

    # Scene 05
    (
        '"Băng dán trạm xá đây nè... con đi truyền dịch hồi nào giấu tao?!"',
        '"Băng dán trạm xá đây nè... truyền dịch hồi nào giấu tao?!"'
    ),
    (
        '"Nửa đêm Duyên sốt bốn mươi độ... nó cắn răng chịu không dám phiền má!"',
        '"Nửa đêm Duyên sốt cao... cắn răng chịu không dám phiền má!"'
    ),
    (
        '“ Băng dán trạm xá đây nè... con đi truyền dịch hồi nào giấu tao?! ”',
        '“ Băng dán trạm xá đây nè... truyền dịch hồi nào giấu tao?! ”'
    ),
    (
        '“ Nửa đêm Duyên sốt bốn mươi độ... nó cắn răng chịu không dám phiền má! ”',
        '“ Nửa đêm Duyên sốt cao... cắn răng chịu không dám phiền má! ”'
    ),

    # Scene 08
    (
        '"Đem ra hàng ba mắc nghen con... trưa má nằm canh chừng!"',
        '"Đem ra hàng ba mắc nghen... trưa má nằm canh chừng!"'
    ),
    (
        '"Dạ má! Con mắc ngoài hiên đón gió... để má nghỉ ngơi nghen!"',
        '"Dạ má! Con mắc ngoài hiên... để má nằm đón gió mát!"'
    ),
    (
        '“ Đem ra hàng ba mắc nghen con... trưa má nằm canh chừng! ”',
        '“ Đem ra hàng ba mắc nghen... trưa má nằm canh chừng! ”'
    ),
    (
        '“ Dạ má! Con mắc ngoài hiên đón gió... để má nghỉ ngơi nghen! ”',
        '“ Dạ má! Con mắc ngoài hiên... để má nằm đón gió mát! ”'
    ),

    # Scene 10
    (
        '"Bà Ba ơi! Tui mang rượu gừng qua xức cho thằng Tin nè!"',
        '"Bà Ba ơi! Tui mang rượu gừng qua xức cho Tin nè!"'
    ),
    (
        '"Khỏi đi chị Tám! Cháu tui nằm nôi phẳng, da non cấm xức rượu!"',
        '"Khỏi đi chị Tám! Cháu tui nằm nôi, cấm xức rượu cay!"'
    ),
    (
        '“ Bà Ba ơi! Tui mang rượu gừng qua xức cho thằng Tin nè! ”',
        '“ Bà Ba ơi! Tui mang rượu gừng qua xức cho Tin nè! ”'
    ),
    (
        '“ Khỏi đi chị Tám! Cháu tui nằm nôi phẳng, da non cấm xức rượu! ”',
        '“ Khỏi đi chị Tám! Cháu tui nằm nôi, cấm xức rượu cay! ”'
    ),
]

for old_s, new_s in replacements:
    if old_s in text:
        text = text.replace(old_s, new_s)
        print(f"Replaced: {old_s[:30]}... -> {new_s[:30]}...")
    else:
        print(f"NOT FOUND: {old_s[:30]}...")

with open(tap1_path, "w", encoding="utf-8") as f:
    f.write(text)

print("[+] Done updating quotes in tap-1.html")
