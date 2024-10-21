from jinja2 import Template

template_content = open('property_template.py.jinja').read()
template = Template(template_content)

factors = {
    'op_creation': {
        "random": "random.random()",
        "uniform": "random.uniform(0, 1)",
        "uniform10": "random.uniform(0, 10)",
        "uniform100": "random.uniform(0, 100)",
        "numpy": "np.random.rand()"
    },
    'op_compare': {
        "tolerance15": "result1 - result2 < 1e-15",
        "tolerance16": "result1 - result2 < 1e-16",
        "tolerance18": "result1 - result2 < 1e-18",
        "equal": "result1 == result2",
    }
}

all_factors = {}
for k1, v1 in factors['op_creation'].items():
    for k2, v2 in factors['op_compare'].items():
        all_factors[k1 + '_' + k2] = {
            'op_creation': v1,
            'op_compare': v2
        }

print("experiments;op_creation;op_compare;result")
for key, factor in all_factors.items():
    generated_code = template.render(factor)
    print(f"{key};{factor['op_creation']};{factor['op_compare']};", end="")
    exec(generated_code)
