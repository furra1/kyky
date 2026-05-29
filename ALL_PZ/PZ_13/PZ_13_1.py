# Задание (вариант 15): В исходном текстовом файле (radio_stations.txt) найти все
# домены из URL-адресов.

import os
import re

file_path = os.path.join(os.path.dirname(__file__), 'radio_stations.txt')

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

url_pattern = re.compile(
    r'https?://(?:[\w.-]+@)?([\w.-]+)(?::\d+)?(?:/[\w./?%&=-]*)?',
    re.IGNORECASE,
)

domains = []
for match in url_pattern.finditer(text):
    domain = match.group(1)
    if domain not in domains:
        domains.append(domain)

print("Исходный файл:")
print(text)
print("Найденные домены:")
for domain in domains:
    print(domain)
print(f"\nКоличество доменов: {len(domains)}")

with open(os.path.join(os.path.dirname(__file__), 'domains_result.txt'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(domains))

print("Результат записан в domains_result.txt")
