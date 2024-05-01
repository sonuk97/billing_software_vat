from django.contrib import admin
from django.urls import path, include
from BillApp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('blog',views.goBlog, name='goBlog'),
    path('login',views.login, name='login'),
    path('register_user',views.registerUser, name='registerUser'),
    path('register_trial_user',views.registerTrialUser, name='registerTrialUser'),
    path('user_login',views.userLogin, name='userLogin'),
    path('logout',views.userLogout, name='userLogout'),
    path('validate_email',views.validateEmail, name='validateEmail'),
    path('validate_username',views.validateUsername, name='validateUsername'),
    path('validate_phone_number',views.validatePhone, name='validatePhone'),
    path('validate_company_name',views.validateCompany, name='validateCompany'),
    path('forgot_password',views.forgotPassword, name='forgotPassword'),
    path('show_profile',views.showProfile, name='showProfile'),
    path('update_user_profile',views.updateUserProfile, name='updateUserProfile'),
    path('update_logo/<int:id>',views.updateLogo, name='updateLogo'),
    path('remove_company_logo',views.removeLogo, name='removeLogo'),


    path('go_dashboard', views.goDashboard, name='goDashboard'),
    path('redirect_page',views.redirectPage, name='redirectPage'),

    path('show_items',views.goItems, name='goItems'),
    path('show_item_details/<int:id>',views.showItemData, name= 'showItemData'),
    path('check_item_name',views.checkItemName, name='checkItemName'),


    path('show_purchases',views.goPurchases, name='goPurchases'),
    path('add_new_purchase',views.addNewPurchase, name='addNewPurchase'),
    path('get_item_data',views.getItemData, name='getItemData'),
    path('create_new_purchase',views.createNewPurchase, name='createNewPurchase'),
    path('purchases_in_between',views.purchasesInBetween, name='purchasesInBetween'),
    path('view_purchase_bill/<int:id>',views.viewPurchaseBill, name='viewPurchaseBill'),
    path('edit_purchase_bill/<int:id>',views.editPurchaseBill, name='editPurchaseBill'),
    path('update_purchase_bill/<int:id>',views.updatePurchaseBill, name='updatePurchaseBill'),
    path('delete_purchase_bill/<int:id>',views.deletePurchaseBill, name='deletePurchaseBill'),
    


    path('show_sales',views.goSales, name='goSales'),
    path('add_new_sale',views.addNewSale, name='addNewSale'),
    path('create_new_sale',views.createNewSale,name='createNewSale'),
    path('sales_in_between',views.salesInBetween, name='salesInBetween'),
    path('view_sales_bill/<int:id>',views.viewSalesBill, name='viewSalesBill'),
    path('edit_sales_bill/<int:id>',views.editSalesBill, name='editSalesBill'),
    path('update_sale_bill/<int:id>',views.updateSaleBill, name='updateSaleBill'),
    path('delete_sale_bill/<int:id>',views.deleteSaleBill, name='deleteSaleBill'),
    path('sales_bill_pdf/<int:id>',views.salesBillPdf, name='salesBillPdf'),
    path('share_sales_bill_to_email/<int:id>',views.shareSalesBillToEmail, name= 'shareSalesBillToEmail'),


    path('add_new_item',views.addNewItem, name='addNewItem'),
    path('delete_item/<int:id>',views.deleteItem, name='deleteItem'),
    path('edit_item/<int:id>',views.editItem, name='editItem'),
    path('edit_item_data/<int:id>',views.editItemData, name='editItemData'),
    path('create_new_item',views.createNewItem, name='createNewItem'),
    path('create_new_itemunit',views.createitemunit, name='createitemunit'),
    path('get_item_units',views.getItemUnits, name='getItemUnits'),
    path('update_stock/<int:id>',views.updateStock, name='updateStock'),


    path('edit_transaction/<int:id>',views.editTransaction, name='editTransaction'),
    path('edit_transaction_data/<int:id>',views.editTransactionData, name='editTransactionData'),
    path('delete_transaction/<int:id>',views.deleteTransaction, name='deleteTransaction'),

    path('stock_reports',views.goStockReports, name='goStockReports'),
    path('item_stock_report/<int:id>',views.itemStockReport, name='itemStockReport'),
    path('share_stock_report_to_email',views.shareStockReportsToEmail, name='shareStockReportsToEmail'),

    path('change_trial_status/<str:status>',views.changeTrialStatus, name='changeTrialStatus'),
    
    #ADMIN PANEL -- URLS
    path('go_registered_clients',views.goRegisteredClients, name='goRegisteredClients'),
    path('go_demo_clients',views.goDemoClients, name='goDemoClients'),
    path('go_purchased_clients',views.goPurchasedClients, name='goPurchasedClients'),
    path('cancel_subscription/<int:id>',views.cancelSubscription, name='cancelSubscription'),
    path('go_payment_terms',views.goPaymentTerms, name='goPaymentTerms'),
    path('add_new_payment_term',views.addNewPaymentTerm, name='addNewPaymentTerm'),
    path('create_payment_term',views.createPaymentTerm, name='createPaymentTerm'),
    path('delete_payment_term/<int:id>',views.deletePaymentTerm, name='deletePaymentTerm'),
    path('client_purchase/<int:id>',views.clientPurchase, name='clientPurchase'),
    path('get_payment_terms',views.getPaymentTerms, name='getPaymentTerms'),
    path('remove_user/<int:id>',views.removeUser, name='removeUser'),
    
    
    path('sales_report',views.sales_report, name='sales_report'),
    path('shareSalesReportsToEmail',views.shareSalesReportsToEmail, name='shareSalesReportsToEmail'),
    path('salesreport_graph',views.salesreport_graph, name='salesreport_graph'),
]