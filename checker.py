import json
from pprint import pprint
from api.modules.documents.crud import get_next_undone_in_queue
from docx import Document

from docx.shared import Pt, RGBColor
from docx.document import Document as DocumentType
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_COLOR_INDEX

from api.modules.docrules.schemas import TextFormatRules
from api.modules.docrules.crud import get_value_by_id

from api.modules.documents.routes import FILES_DIR
from api.modules.docrules.routes import RULES_FILES_DIR
import os, os.path as op

RESULTS_FILES_DIR = os.path.join(os.getcwd(), 'results')

def checker():
    while True:
        doc = get_next_undone_in_queue()
        if doc:
            result_file = fix_document(doc.doc_name, doc.doc_type.rules_file)
            doc.done = True
            doc.result = result_file
            doc.save()

def fix_document(document_name: str, rules_file: str) -> str:
    document: DocumentType = Document(op.join(FILES_DIR, document_name))
    rules_dict: list[dict] = json.load(open(op.join(RULES_FILES_DIR, rules_file), 'r'))
    rules: list[TextFormatRules] = [TextFormatRules.model_validate(rule) for rule in rules_dict]

    # Iterate rules list and group it by name property
    rules_grouped: dict[str, list[TextFormatRules]] = {}
    for rule in rules:
        text_type = rule.text_type
        if text_type not in rules_grouped:
            rules_grouped[text_type] = []
        rules_grouped[text_type].append(rule)

    # Create custom styles
    for k, v in rules_grouped.items():
        custom_style = document.styles.add_style(f"Custom {k}", WD_STYLE_TYPE.PARAGRAPH)
        if k.startswith('Heading'):
            custom_style.base_style = document.styles[k] # type: ignore
        for rule in v:
            match rule.name:
                case 'font-size':
                    custom_style.font.size = Pt(float(rule.value)) # type: ignore
                case 'font-family':
                    value = get_value_by_id(int(rule.value))
                    custom_style.font.name = value.value # type: ignore
                case 'bold':
                    custom_style.font.bold = rule.value=='1' # type: ignore
                case 'italic':
                    custom_style.font.italic = rule.value=='1' # type: ignore
                case 'underline':
                    custom_style.font.underline = rule.value=='1' # type: ignore
                case 'color':
                    value = get_value_by_id(int(rule.value))
                    match value.value:
                        case 'black':
                            custom_style.font.color.rgb = RGBColor(0, 0, 0) # type: ignore
                        case 'red':
                            custom_style.font.color.rgb = RGBColor(255, 0, 0) # type: ignore
                        case 'green':
                            custom_style.font.color.rgb = RGBColor(0, 255, 0) # type: ignore
                        case 'blue':
                            custom_style.font.color.rgb = RGBColor(0, 0, 255) # type: ignore
                case 'background-color':
                    value = get_value_by_id(int(rule.value))
                    match value.value:
                        case 'black':
                            custom_style.font.highlight_color = WD_COLOR_INDEX.BLACK # type: ignore
                        case 'red':
                            custom_style.font.highlight_color = WD_COLOR_INDEX.RED # type: ignore
                        case 'green':
                            custom_style.font.highlight_color = WD_COLOR_INDEX.GREEN # type: ignore
                        case 'blue':
                            custom_style.font.highlight_color = WD_COLOR_INDEX.BLUE # type: ignore
                case 'alignment':
                    value = get_value_by_id(int(rule.value))
                    match value.value:
                        case 'left':
                            custom_style.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.LEFT # type: ignore
                        case 'center':
                            custom_style.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER # type: ignore
                        case 'right':
                            custom_style.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT # type: ignore
                        case 'justify':
                            custom_style.paragraph_format.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY # type: ignore
                case 'subscript':
                    custom_style.font.subscript = rule.value=='1' # type: ignore
                case 'superscript':
                    custom_style.font.superscript = rule.value=='1' # type: ignore

    # Apply the custom style to a paragraph
    for paragraph in document.paragraphs:
        if rules_grouped.get(paragraph.style.name): # type: ignore
            paragraph.style = document.styles[f"Custom {paragraph.style.name}"] # type: ignore

    # Save the modified document
    result_file = 'fixed_' + document_name
    document.save(op.join(RESULTS_FILES_DIR, result_file))
    print(f"Fixed file {op.join(FILES_DIR, document_name)}. Result saved in {op.join(RESULTS_FILES_DIR, result_file)}")
    return result_file

if __name__=='__main__':
    # fix_document('test.docx', 'test.json')
    checker()