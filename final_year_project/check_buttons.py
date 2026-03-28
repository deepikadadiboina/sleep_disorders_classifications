import glob, re
files = sorted(set(glob.glob('*.py') + glob.glob('pages/*.py') + glob.glob('utils/*.py')))
print('Files checked:', len(files))
print('---')
for f in files:
    txt = open(f, encoding='utf8').read()
    button_count = len(re.findall(r'st\.button\(', txt))
    key_count = len(re.findall(r'st\.button\([^)]*key\s*=\s*', txt))
    print(f'{f}: buttons={button_count}, with_key={key_count}, missing_key={button_count-key_count}')
    if button_count - key_count > 0:
        print('  first 5 no-key buttons:', [line.strip() for line in txt.splitlines() if 'st.button(' in line and 'key=' not in line][:5])
