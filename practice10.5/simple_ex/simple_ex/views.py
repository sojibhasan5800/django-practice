from django.shortcuts import render

def homepage(request):
    back={
       'foods':[
           {
        'meal':'vagi',
        'id' :5,
        'ammount':100,

        'meal':'gajor',
        'id' :10,
        'ammount':100,

        'meal':'komra',
        'id' :15,
        'ammount':100
           },'alog'
       ],

        'course':[
            {
            'course_name':'python',
            'id' :105,
            'ammount':2000,
            'course_name':'django',
            'id' :105,
            'ammount':2000,
            'course_name':'html',
            'id' :105,
            'ammount':2000,
            }
        ]
    }
    return render(request,'home.html',context=back)