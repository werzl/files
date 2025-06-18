import re

def line_items_to_list(input_object, params, output_object=[]):
    for param_name in params:
        if param_name == 'product_name': # Use this if you expect commas in the values.
            matches = re.findall(r'\d*,0*(,0*)* Files', input_object[param_name])
            for match in matches:
                decimal = match.replace(',', '.')
                input_object[param_name] = input_object[param_name].replace(
                    match, decimal)

        array = input_object[param_name].split(',')

        for i, array_item in enumerate(array):
            if param_name == 'product_name': # Use this if you expect commas in the values.
                matches = re.findall(r'\d*.0*(.0*)* Files', array_item)
                for match in matches:
                    comma = match.replace('.', ',')
                    array_item = array_item.replace(match, comma)

            if 0 <= i < len(output_object):
                output_object[i][param_name] = array_item
            else:
                output_object.insert(i, {param_name: array_item})

    return output_object