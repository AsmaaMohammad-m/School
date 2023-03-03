from odoo import models , fields,api,_
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
class school_itemt(models.Model):
    _name='school.item'
    student_id=fields.Many2one('school.student',string="Student")
    class_id=fields.Integer(string="Class ID",related="student_id.class_id")

    division=fields.Char(string="Division",related="student_id.division")
    admission_date = fields.Date(string="Admission date", related="student_id.admission_date")
    product_ids=fields.Many2many('product.product',string="Items")
