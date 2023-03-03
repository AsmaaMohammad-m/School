from odoo import models , fields,api,_
from datetime import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
from odoo.exceptions import UserError
class ResPartner(models.Model):
    _inherit='res.partner'
    date_of_birth=fields.Date('DOB')
                              #,default=fields.Date.today())

   
    
    

    @api.model_create_multi
    def create(self, vals_list):
        """ We don't want the current user to be follower of all created job """
        for vals in vals_list:
            vals['date_of_birth']=fields.Date.today()
            res=super(ResPartner,self).create(vals_list)
        return res

    @api.model
    def _name_search(self,name,args=None,operator='ilike',limit=100,name_get_uid=None):
        args=args or []
        domain=[]
        if name:
            domain=["|","|",('name',operator,name),('phone',operator,name),('email',operator,name)]
        return self._search(domain+args,limit=limit,access_rights_uid=name_get_uid)
