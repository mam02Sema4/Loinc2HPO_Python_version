import sys
import click
from seep_hpo.util.AnnotationParser import AnnotationParser
from seep_hpo.util.AnnotationResolver import AnnotationResolver
from seep_hpo.util.QueryFileParser import QueryFileParser

@click.group()
def cli():
    pass


@cli.command()
@click.argument('annotation_path', type=click.Path(exists=True))
@click.argument('query_path', type=click.Path(exists=True))
@click.option('--report', default='tsv', help='Format to report in. One of (json, csv, tsv).'
                                              'Default: tsv')
def resolve(annotation_path, query_path, report_format):
    """Command to resolve loinc 2 hpo mappings.

    ANNOTATION_PATH is the path to the LOINC HPO Annotation File.
    QUERY_PATH is the path to your file with Loinc Id's, Measures, Negations.
    """
    click.echo('Parsing annotation files...')
    click.echo(click.format_filename(annotation_path))
    click.echo(click.format_filename(query_path))
    annotations = AnnotationParser.parse_annotation_file_dict(annotation_path)
    queries = QueryFileParser.parse(query_path)
    resolver = AnnotationResolver(annotations)
    click.echo('Resolving your queries...')
    for query in queries:
        result = resolver.resolve(query)
        if report_format == 'json':
            print('{{0}:{{1}:{{2}:{3}}}}'.format(query.loinc_id, query.measure, query.negated,
                                                 result))
        elif report_format == 'csv':
            print('{0},{1},{2},{3}'.format(query.loinc_id, query.measure, query.negated, result))
        else:
            print('{0}\t{1}\t{2}\t{3}'.format(query.loinc_id, query.measure, query.negated, result))


@cli.command()
def version():
    """Command to check the version of LOINC2HPO"""
    click.echo("Version not configured yet.")


if __name__ == '__main__':
    sys.exit(cli())
