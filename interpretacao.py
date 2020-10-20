def interpretacao_ml(x_train, plot_n_variaveis = 15, modelo = "RF",objeto_modelo):

	if type_model == "RF":
		shap_values_train = shap.TreeExplainer(objeto_modelo, model_output = 'margin').shap_values(x_train)
		shap.summary_plot(shap_values_train[1], features = x_train, max_display = plot_n_variables, plot_type = ['dot','bar'][0])

	if type_model == "CAT_BOOST":
		shap_values = objeto_modelo.get_feature_importance(Pool(x_train, y_train), type = 'ShapValues')
		expected_value = shap_values[0,-1]
		shap_values = shap_values[:,:-1]
		shap.summary_plot(shap_values, features = x_train, max_display = plot_n_variables, plot_type = ['dot','bar'][0])

	if type_model == "XGB":
		shap_values_train = shap.TreeExplainer(objeto_modelo, model_output = 'margin').shap_values(x_train)
		shap.summary_plot(shap_values_train, features = x_train, max_display = plot_n_variables, plot_type = ['dot','bar'][0])

	if type_model == "LBGM":
		shap_values_train = shap.TreeExplainer(objeto_modelo, model_output = 'margin').shap_values(x_train)
		shap.summary_plot(shap_values_train[1], features = x_train, max_display = plot_n_variables, plot_type = ['dot','bar'][0])

	else:
		print("Modelo não identi")