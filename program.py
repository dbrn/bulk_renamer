from string import Template
from pathlib import Path
from glob import glob

# I made this program to try the class Template from the module string
# It takes a path as an input and a filename pattern, for each # in the pattern
# we'll have a number. Eg: pattern###.jpg => pattern001.jpg


def main():
    path = input("Input the path where the files are: ")
    file_pattern = input("Input the file-pattern (eg. pic####.ext): ")

    # find the index of the first # and the index of the last #
    # and the length of the # sequence
    index = file_pattern.index("#")
    index_r = file_pattern.rindex("#")
    len_hashtag = len(file_pattern[index:index_r + 1])

    # create a dictionary and a template for the files to be renamed
    template_dict = dict(path=path, name=file_pattern[0:index], ext=file_pattern[index_r + 1:], num="")
    template = Template("$path$name$num$ext")

    # find all the files in the path contained in the variable path
    files = glob(f"{path}*.*")
    counter = 1

    # for each file found in the path...
    for file in files:

        # count how many zeros must be written before our counter
        if len(str(counter)) < len_hashtag:
            num_string = (len_hashtag - len(str(counter))) * "0" + str(counter)
        else:
            num_string = str(counter)

        # update the dict with the counter string we just calculated
        template_dict["num"] = num_string

        # create a Path object with the file's path and rename it according to
        # our dictionary
        p = Path(file)
        p.rename(template.substitute(template_dict))
        counter += 1


if __name__ == "__main__":
    main()
