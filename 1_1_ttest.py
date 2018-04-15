import numpy as np
def main():
    with open('files/generate_for_ttest.txt', 'r', encoding='utf8') as source:
        contents = (source.readlines())
        contents = [float(content.strip()) for content in contents]
        contents = contents[:10]
        contents = np.array(contents)
    print(contents)

    mean = contents.mean()
    std = np.std(contents)

    result = (mean - 0.5)/(std/np.sqrt(10))

    print(mean)
    print(std)

    print(result)

if __name__ == '__main__':
    main()
