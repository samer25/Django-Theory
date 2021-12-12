"""
Unit vs Integration Testing

Unit test:
-isolated coded i.e., specific function
-Faster Execution
-More in number
-Practical for pure functions
-String transformations
-Validators

Integration tests
-Entire application flow i.e., integration of functions
-Slower execution
-Less in number
-Practical for user stories
    -User registration
    -Course signup after payment


Best Practices

If a piece of code can break, you must test it
Each test should:
-Cover only one function (unit) or flow (integration)
-Assert only one case
Keep it simple
Arrange,Act, Assert

Structure

There are several ways to write tests
-Putting everything in the tests.py file and grouping test by they test(models, views, forms, etc.)
-Or crating a older test with the different test files for different functionality that they test(test_form.py,
 test_models.py, test_view.py, etc.)

What should be tested?
(From a software developer)

Put simply all aspects of the code
-Models/Managers
-Forms
-Views
-Other custom code
Except:
-Built-in code
    -Model.objects.create(), Model.object.all(), etc..
-code from third-party libraries
    - i.e. testing something that comes from library


Testing Models

Testing model definitions is pointless
-i.e. if a CharField is saved as a varchar in the database
In models the only thing that should be tested is the validation
-Except built-in validators
-i.e., providing invalid data should dail the test


Testing Models

class Profile(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(validators=(
        MinValueValidator(0),
        MaxValueValidator(150)
        ))
        egn = models.CharField(max_length=10, validators=[egn_validator])

Testing name and age is pointless
    - They use built-in validators
Only egn should be tested

Models are tested as follows:

def test_profileCreate_whenInvalidEgn_shouldRaise(self):
    p = Profile(name='Sammy Mahamid', age=19, egn='323432a4321)
    try:
        p.full_clean()
        p.save()
        self.fail()
    except ValidationError as ex:
        self.assertIsNotNone(ex)

def test_profileCreate_whenValidEgn_shouldCreateIt(self):
    p = Profile(name='Sammy Mahamid', age=18, egn=231456329)
    p.full_clean()
    p.save
    self.assertIsNotNone(p)


Testing Forms

Testing forms is pretty much the same as testing models
-only test the custom (your) logic

def test_profileFormSave_whenValid_xxx(self):
    data = {
        'name': 'Sammy Mahamid',
        'age': 18,
        'egn': '3242143213'
        }
    form = ProfileForm(data)
    self.assertTrue(form.is_valid())


def test_profileFormSave_whenInvalid_xxxx(self):
    data = {
        'name': 'Sammy Mahamid',
        'age': 18,
        'egn': '32421a3213'
        }
    form = ProfileForm(data)
    self.assertFalse(form.is_valid())



Views Testing

Views are tested using a test client
-"Sends" requests to your views by URL
-Asserts templates, context, redirect, status, code
-logins user and persist session
    -This for the next course

class ProfileViewTest(TestCase):
    def setUp(self):
        self.test_client = Client()


Testing Views GET Examples

Render template

def test_getProfilesIndex_shouldRenderTemplate(self):
    response = self.test_client.get(')
    self.assertTemplateUsed(response, 'testing/index.html')

Context data

def test_getProfilesIndex_shouldReturnCorrectContext(self):
    response = self.test_client.get('')
    profiles = response.context['profiles']
    self.assertNotNone(profiles)


Testing Views POST Examples

Render template

def test_profilesIndex_whenValidData_shouldCreateAndRedirectToIndex(self):
    data = {
        'name': 'Sammy'
        'age': 19,
        'egn': '2345329403'
    }
    response = self.test_client.post('/', data)
    self.assertRedirects(response, '/')

Testing Other Code

Given the validator:

def egn_validator(value: str):
    result = all(d.isdigits() for d in value)
    if not result:
        raise ValidatorError('egn should contain only digits')

The test:

def test_egnValidator_whenAllIsDigits_shouldDoNothing(self):
    egn_validator('1234567890')
    self.assertTrue(True)

def test_egnValidator_whenOneNoDigit_shouldRaise(self):
    with self.assertRaise(ValidationError) as context:
        egn_validator(12345a32223)
    self.assertIsNotNone(context.exception)


Final Notes

All model, fom and view test are integration tests
    -They depend on Django itself se making them unit tests is impossible
Validation test can be unit test
-If they do not have external dependencies
-Or if mocking their external dependencies
The bigger the flow of an integration test the more unit test and smaller integration test become redundant
    -i.e., view test cover forms and models as well
"""