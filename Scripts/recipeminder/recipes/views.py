from django.shortcuts import render, HttpResponse, redirect
from recipes.models import Recipe
from recipes.forms import RecipeForm

def recipe_list(request):
	recipelist = Recipe.objects.all()
	context = {'recipelist': recipelist}
	return render(request, 'recipelist.html', context)

def recipe(request, recipe_id):
	try:
		recipe = Recipe.objects.get(id = recipe_id)
	except Recipe.DoesNotExist:
		raise Http404
	context = {'recipe' : recipe}
	return render(request, 'recipe.html', context)

def addrecipe(request):
	if request.method == 'POST':
		form = RecipeForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			r = Recipe()
			r.name = data['name']
			r.servings = data['servings']
			r.ingredients = data['ingredients']
			r.instructions = data['instructions']
			r.save()
			return redirect(recipe_list)
	else:
		form = RecipeForm()
	return render(request, 'addrecipe.html', { 'form': form })