from lesson8.modules.company_api import CompanyApi

api = CompanyApi('https://x-clients-be.onrender.com')

# def test_get_companies():
#   body = api.get_company_list()
  
#   assert len(body) > 0
  
# def test_get_active_companies():
#   # get all companies
#   full_list = api.get_company_list()
  
#   # get active companies
#   filtered_list = api.get_company_list(params_to_add = {'active': 'true'})
  
#   assert len(full_list) > len(filtered_list)
  
# def test_add_company():
#   company_name = 'sky'
#   company_desc = 'sky about'
#   # получить список компаний
#   body_before = api.get_company_list()
#   len_before = len(body_before)
#   # добавить компанию
#   result = api.create_company(name = company_name, description = company_desc  )
#   new_id = result['id']
#   # получить список компаний
#   body_after = api.get_company_list()
#   len_after  = len(body_after)

#   assert len_after - len_before == 1
#   assert body_after[-1]['name'] == company_name
#   assert body_after[-1]['description'] == company_desc
#   assert body_after[-1]['id'] == new_id
  
# def test_get_company_by_id():
#   name = 'sky'
#   descr = 'descr'
#   result = api.create_company(name, descr)
#   new_id = result['id']
  
#   new_company = api.get_company_by_id(new_id)

#   assert new_company['id'] == new_id
#   assert new_company['name'] == name
#   assert new_company['description'] == descr
  
# def test_edit_company():
#   name = 'name for edit',
#   descr = 'descr for edit'
#   company = api.create_company(name, descr)
#   id = company['id']
  
#   new_name = 'new name'
#   new_descr = 'new descr'
#   edited_company = api.edit_company(id, new_name, new_descr)
  
#   assert id == edited_company['id']
#   assert new_name == edited_company['name']
#   assert new_descr == edited_company['description']
  
# def test_delete_company():
#   company_name = 'sky1'
#   company_descr = 'sky about'
#   company = api.create_company(name = company_name, description = company_descr)
#   id = company['id']

#   deleted = api.delete_company(id)
#   assert deleted['id'] == id
#   assert deleted['name'] == company_name
#   assert deleted['description'] == company_descr
  
#   print(api.get_company_by_id(id))
#   body = api.get_company_list()
#   assert body[-1]['id'] != id
  
# def test_deactivated_company():
#   status = False
#   created = api.create_company('company')
  
#   deactivated = api.set_status(created['id'], status)
  
#   assert deactivated['isActive'] == status

# def test_activated_company():
#   created = api.create_company('company')
  
#   api.set_status(created['id'], False)
  
#   activated = api.set_status(created['id'], True)
  
#   assert activated['isActive'] == True 