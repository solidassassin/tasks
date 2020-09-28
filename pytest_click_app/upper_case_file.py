import click


@click.command()
@click.option(
    "--input-file",
    type=click.Path(exists=True, readable=True),
    required=True,
    help="Input text file path",
)
@click.option(
    "--output-file",
    type=click.Path(writable=True),
    required=True,
    help="Output text file path",
)
def upper_case_file(input_file, output_file):
    print(f"Converting {input_file} file to upper case in {output_file}!")

    with open(input_file, "r") as input_f:
        with open(output_file, "w") as output_f:
            output_f.write(input_f.read().upper())

    print("Done!")


if __name__ == '__main__':
    upper_case_file()
