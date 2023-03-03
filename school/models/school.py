from odoo import models , fields,api,_
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError

class school_student(models.Model):
    _name='school.student'
    name=fields.Many2one('res.partner',string='Student Name')
    class_id=fields.Integer(string="Class ID")
    address=fields.Char(string="Address")
    division=fields.Char(string="Division")
    birth_date=fields.Date(string="Birth Date")
    age=fields.Integer(string="Age",compute='_compute_age')
    date=fields.Date()
    officer=fields.Many2one('res.users',default=lambda  self:self.env.user)

    admission_date=fields.Date(string="Admission date",default=fields.Date.today())
    admission_code=fields.Char(string="Admission Code",default=lambda self:_('New'))
    subjects = fields.Many2many('school.subject', string="Subjects")
    def unlink(self):
        raise UserError(_('Sorry you can not delete this student'))
        return super(school_student, self).unlink()

    @api.onchange('name')
    def _on_change_name(self):

        self.address=self.name.street
        self.birth_date=self.name.date_of_birth

    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:

            record.age=relativedelta(datetime.today(),record.birth_date).years

    @api.constrains('birth_date')
    def validation_constraints(self):
        today=fields.Date.today()
        for rec in self:

            if rec.birth_date>today:
                raise ValidationError(_('Invalid date of birth ..please enter correct date'))
            elif (rec.class_id>200)or(rec.class_id<1):
                raise ValidationError(_('Sorry class can not be greater than 200 or less than 1'))
    _sql_constraints=[('unique_code','unique(admission_code)','This code is exist....')]

    @api.model
    def create(self,vals_list):
        if vals_list.get('admission_code','New')=='New':
            vals_list['admission_code']=self.env['ir.sequence'].next_by_code('school.student.sequence') or 'New'
            result=super(school_student,self).create(vals_list)
            return result