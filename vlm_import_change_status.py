from selenium import webdriver
import time

#driver = webdriver.Ie(executable_path= r'D:\...\IEDriverServer.exe')
driver = webdriver.Firefox(executable_path=r'D:\...\geckodriver.exe')
driver.maximize_window()
driver.get('link_login')

time.sleep(3)

username = driver.find_element_by_id('userId')
username.send_keys('username')

password = driver.find_element_by_id('password')
password.send_keys('Password')

#otp = driver.find_element_by_id('otpPassword')
#otp.click()

time.sleep(10)

btnLogin = driver.find_element_by_id('btnLogin')
btnLogin.click()

time.sleep(5)

'''
driver.get('http://link_import')

time.sleep(3)

dirCSV = driver.find_element_by_id('csvFile')
dirCSV.send_keys('D:\...\CSV_FILE.csv')

useConfigFile_checkbox = driver.find_element_by_css_selector('#configFileSection input#useConfigFile')
useConfigFile_checkbox.click()

dirConfigFile = driver.find_element_by_id('configFile')
dirConfigFile.send_keys('D:\...\BulkCreate-configuration-20180'
                        '7061928.txt')

btnNext_step = driver.find_element_by_id('nextButton')
btnNext_step.click()

btnNext_settings_step = driver.find_element_by_css_selector('#jimform #nextButton')
btnNext_settings_step.click()

allMappingCheckBoxes = driver.find_elements_by_css_selector('#fieldMappings input.checkbox.manual-mapping-checkbox')
print(len(allMappingCheckBoxes))

for mappingCheckbox in allMappingCheckBoxes:
    mappingCheckbox.click()

btnNextMapField = driver.find_element_by_css_selector('#jimform #nextButton')
btnNextMapField.click()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

btnNextMapField = driver.find_element_by_css_selector('#jimform #nextButton')
btnNextMapField.click()

#wait for complete import 

linkTextListCreated = driver.find_element_by_link_text('Check created issues.')
linkTextListCreated.click()
'''

driver.get('link_after_issue_ created')

btnTools = driver.find_element_by_css_selector('ul.operations li:nth-child(5)')
btnTools.click()
time.sleep(1)

btnAllIssue = driver.find_element_by_id('bulkedit_all')
btnAllIssue.click()


#driver.get('link select all created issue')


checkAllIssue = driver.find_element_by_id('bulkedit-select-all')
checkAllIssue.click()

btnNextChooseIssueStep = driver.find_element_by_id('next')
btnNextChooseIssueStep.click()

radioTransitionIssues = driver.find_element_by_id('bulk.workflowtransition.operation.name_id')
radioTransitionIssues.click()

btnNextChooseOperation = driver.find_element_by_id('next')
btnNextChooseOperation.click()


radioAssignIssue = driver.find_element_by_id('id_WORKLIST Daily Workflow_711_10852')
radioAssignIssue.click()

btnNextChooseIssueStep = driver.find_element_by_id('next')
btnNextChooseIssueStep.click()

linkTextAssignToMe = driver.find_element_by_id('assign-to-me-trigger')
linkTextAssignToMe.click()

btnNextChooseIssueStep = driver.find_element_by_id('next')
btnNextChooseIssueStep.click()

btnConfirm = driver.find_element_by_id('next')
btnConfirm.click()

#need wait for change status complete

btnAcknolege = driver.find_element_by_id('acknowledge_submit')
btnAcknolege.click()

'''
radioResolveIsse = driver.find_element_by_id('id_WORKLIST Daily Workflow_5_5')

radioStartProgress = driver.find_element_by_id('id_WORKLIST Daily Workflow_4_3')

listBoxResolution = driver.find_element_by_id('resolution')

#Resolution = Fix
fixResolution = driver.find_element_by_css_selector('select#resolution option:nth-child(2)')

'''
