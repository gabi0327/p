from django.shortcuts import render

# Lista persistente en memoria (se mantendrá mientras el servidor esté en ejecución)
personas_registradas = []

def inicio(request):
    global personas_registradas
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '').strip()
        carnet = request.POST.get('carnet', '').strip()
        
        if nombre and carnet:  # Validamos que no estén vacíos
            nueva_persona = {'nombre': nombre, 'carnet': carnet}
            personas_registradas.append(nueva_persona)
    
    return render(request, 'inicio.html', {'personas': personas_registradas})