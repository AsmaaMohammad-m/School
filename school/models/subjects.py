from odoo import models , fields,api,_
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
class school_subject(models.Model):
    _name='school.subject'
    name=fields.Char(string='Subject Name')
    description=fields.Text(string='Subject Description')