def main():
    with open('files/generate.txt', 'r', encoding='utf8') as sources:
        contents = sources.readlines()
        contents = [content.strip() for content in contents]
        contents.sort(reverse=True)
        with open('files/generate_for_ttest.txt', 'w', encoding='utf8') as writer:
            writer.write('\n'.join(contents[:30]))

    with open('files/original.txt', 'r', encoding='utf8') as sources:
        contents = sources.readlines()
        contents = [content.strip() for content in contents]
        contents.sort(reverse=True)
        with open('files/original_for_ttest.txt', 'w', encoding='utf8') as writer:
            writer.write('\n'.join(contents[:30]))

if __name__ == '__main__':
    main()
