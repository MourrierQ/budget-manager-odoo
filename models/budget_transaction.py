from odoo import fields, models, api
from odoo.addons import decimal_precision as dp

class BudgetTransaction(models.Model):
    _name = 'budget.transaction'
    _rec_name = 'name'

    name = fields.Char('From')

    amount = fields.Float('Amount')
    
    budget_category_id = fields.Many2one(
        'budget.category',
        'Transaction Category'
    )

    category_name = fields.Char(related='budget_category_id.category_name')

    start_date = fields.Date(
        'Begin'
        )
    
    end_date = fields.Date(
        'End'
        )

    # @api.multi
    # def name_get(self):
    #     for transaction in self:
    #         if not self.name:
    #             return [self.category_name]
            
     