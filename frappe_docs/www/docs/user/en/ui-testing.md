---
add_breadcrumbs: 1
title: Testing
metatags:
 description: >
  Frappe provides some basic tooling to write automated tests. We use Cypress
  for writing Integration Tests.
---

# UI Testing

You can write UI tests using [Cypress](https://cypress.io). It is a NodeJS based
full-stack testing framework which doesn't rely on Selenium.

To write integration tests, create a `.js` file in the `cypress/integration`
directory.

### Example

Here is an example of an integration test to check insertion of a ToDo

```js
context('ToDo', () => {
    before(() => {
        cy.login('Administrator', 'admin');
        cy.visit('/desk');
    });

    it('creates a new todo', () => {
        cy.visit('/app/todo/new-todo-1');
        cy.fill_field('description', 'this is a test todo', 'Text Editor').blur();
        cy.get('.page-title').should('contain', 'Not Saved');
        cy.get('.primary-action').click();
        cy.visit('/desk#List/ToDo');
		cy.location('hash').should('eq', '/app/todo');
        cy.get('.list-row').should('contain', 'this is a test todo');
    });
});
```

### Running Cypress Locally

Cypress uses any chromium based browser installed on your system to run tests.
Every app has it's own cypress test suite. To run test for an app, run the
following command from the `frappe-bench` directory.

```sh
bench --site [sitename] run-ui-tests [app]
```

This will open the Cypress Electron shell where you can run any test manually or
run all of the tests.

<img src="/docs/assets/img/running-cypress-tests.gif" class="screenshot">

You can also run tests in headless mode.

```sh
# run in headless mode
bench --site [sitename] run-ui-tests [app] --headless
```

To enable cypress parallel testing you can pass `--parallel` flag.
More information on how cypress parallel tests work can be found [here](https://docs.cypress.io/guides/guides/parallelization).

```sh
# run tests parallelly
bench --site [sitename] run-ui-tests [app] --parallel
```

### Code Coverage
Code coverage helps to identify which lines of the source code were executed during the tests. In order to measure code coverage, the source code needs to be instrumented and this instrumented source code needs to be integrated with our test runner to collect the coverage and generate a report.

For Cypress tests in Frappe, the `.js` files are instrumented using [Istanbul](https://istanbul.js.org/) and the [Cypress code-coverage plugin](https://github.com/cypress-io/code-coverage) is used to merge coverage from each test and save the combined result.

**Code Instrumentation:**

In order to compute which lines of the source code were executed, additional counters are inserted into the code through **_instrumentation_**. For example:

Before instrumentation:

```bash
function foo(a, b) {
    if (a < b)
        return b - a;
    else
        return a - b;
}
```

After instrumentation:

```bash
cov_1m1jljnmzu();

function foo(a, b) {
    cov_1m1jljnmzu().f[0]++;
    cov_1m1jljnmzu().s[0]++;

    if (a < b) {
        cov_1m1jljnmzu().b[0][0]++;
        cov_1m1jljnmzu().s[1]++;
        return b - a;
    } else {
        cov_1m1jljnmzu().b[0][1]++;
        cov_1m1jljnmzu().s[2]++;
        return a - b;
    }
}
```

When using this modified (instrumented) source code for testing, these counters get incremented as the code is executed, and a coverage object is generated. The Cypress code-coverage plugin then handles the collected coverage and generates coverage reports.

**Generating Code Coverage Report Locally:**

1. Instrument source code using [istanbul/nyc](https://github.com/istanbuljs/nyc) :

   ```bash
   npx nyc instrument -x 'frappe/public/dist/**' -x 'frappe/public/js/lib/**' -x '**/*.bundle.js' --compact=false --in-place frappe
   ```
   This replaces the existing source code in the frappe folder with the instrumented source code. The `-x` flag is used to exclude specified paths. You can also use the `-n` flag to specify paths to be included. See [here](https://github.com/istanbuljs/nyc/blob/master/docs/instrument.md) for more details about the `nyc instrument` command

2. Run Cypress tests:

   ```bash
   bench --site test_site run-ui-tests frappe --with-coverage
   ```

3. Generate report:

   ```bash
   npx nyc report --reporter=text
   ```
   See [here](https://istanbul.js.org/docs/advanced/alternative-reporters/) for alternate report formats

### Testing-Library Queries
You can also use [Testing Library](https://testing-library.com/) queries within your Cypress tests. Testing Library provides testing utilities that:

- Make it easier to write UI tests that resemble the way users interact with the app
- Make it easier to find elements in the DOM without knowing all the implementation details
- Help keep the tests maintainable (so minor refactors don't break tests)

> See [Testing Library Docs](https://testing-library.com/docs/queries/about) for more details about usage

Testing Library provides several queries to find elements on a page. Here are some examples:

- [ByRole](https://testing-library.com/docs/queries/byrole)

  Look [here](https://www.w3.org/TR/html-aria/#docconformance) for table of HTML elements and their default roles

  | Query                                  | Element                                                                                       |
  | -------------------------------------- | --------------------------------------------------------------------------------------------- |
  | `findByRole('button', {name: 'Save'})` | `<button>` with [accessible name](https://www.tpgi.com/what-is-an-accessible-name/) = 'Save'  |
  | `findByRole('checkbox')`               | `<input type=checkbox>`                                                                       |
  | `findByRole('textbox')`                | `<input type=text>`, `<textarea>` _(Also matches other elements with default role='textbox')_ |
  | `findByRole('searchbox')`              | `<input type=search>`                                                                         |
  | `findByRole('listbox')`                | `<select>`, `<datalist>`                                                                      |

- [ByLabelText](https://testing-library.com/docs/queries/bylabeltext)

  | Query                         | Element                                      |
  | ----------------------------- | -------------------------------------------- |
  | `findByLabelText('Optimize')` | element associated with the label 'Optimize' |

- [ByPlaceholderText](https://testing-library.com/docs/queries/byplaceholdertext)

  | Query                           | Element                         |
  | ------------------------------- | ------------------------------- |
  | `findByPlaceholderText('Name')` | element with placeholder='Name' |

- [ByText](https://testing-library.com/docs/queries/bytext)

  | Query                        | Element                                 |
  | ---------------------------- | --------------------------------------- |
  | `findByText('example.json')` | element with textContent='example.json' |

- [ByDisplayValue](https://testing-library.com/docs/queries/bydisplayvalue)

  | Query                            | Element                                                                                                    |
  | -------------------------------- | ---------------------------------------------------------------------------------------------------------- |
  | `findByDisplayValue('Option 1')` | `<select>` with selected `<option>` 'Option 1' _(Also matches `<input>` or `<textarea>` with matching value attribute)_ |

- [ByTitle](https://testing-library.com/docs/queries/bytitle)

  | Query                      | Element                        |
  | -------------------------- | ------------------------------ |
  | `findByTitle('Open Link')` | element with title='Open Link' |

- [ByAltText](https://testing-library.com/docs/queries/byalttext/)
- [ByTestId](https://testing-library.com/docs/queries/bytestid/)
