from odoo import fields, models, api

class BudgetCategory(models.Model):
    _name = 'budget.category'
    _rec_name="category_name"

    category_name = fields.Char(
        'Category',
        required=True
    )

    is_income = fields.Boolean('Income', required=True, default=False)

    mensual = fields.Boolean('Mensual', required=True, default=False)

    