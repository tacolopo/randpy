import textwrap

def format_text_file(input_file, output_file):
    # open the input and output files
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # read the input file line by line
        for line in infile:
            # wrap the line to 78 characters, without breaking words
            wrapped_line = textwrap.fill(line, width=78)
            # write the formatted line to the output file
            outfile.write(wrapped_line + '\n')

# format the text in input.txt and write the formatted text to output.txt
format_text_file('input.txt', 'output.txt')
